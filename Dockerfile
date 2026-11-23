# ===== 阶段 1：构建 Vue 前端 =====
FROM node:20-slim AS frontend
ENV NPM_CONFIG_REGISTRY=https://registry.npmmirror.com \
    NPM_CONFIG_FETCH_RETRIES=5 \
    NPM_CONFIG_FETCH_RETRY_MAXTIMEOUT=120000
WORKDIR /fe
COPY frontend/package.json ./
RUN npm config set registry https://registry.npmmirror.com && \
    npm config set fetch-retries 5 && \
    npm config set fetch-retry-maxtimeout 120000 && \
    npm install --no-audit --no-fund
COPY frontend/ ./
RUN npm run build
# 产物在 /fe/../web/dist → /web/dist

# ===== 阶段 2：Python 应用 + 全套安全工具 =====
FROM python:3.12-slim

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_INDEX_URL=https://repo.huaweicloud.com/repository/pypi/simple \
    PIP_TRUSTED_HOST=repo.huaweicloud.com \
    PIP_TIMEOUT=120 \
    PIP_RETRIES=5

# 系统工具 + 挖洞常用工具
RUN apt-get update && apt-get install -y --no-install-recommends \
        curl wget git ca-certificates \
        nmap \
        python3-pip \
        jq dnsutils iputils-ping netcat-openbsd \
        whatweb nodejs \
    && rm -rf /var/lib/apt/lists/*

# sqlmap：官方 PyPI 月度版。构建不依赖 git clone GitHub（国内常超时/失败），
# 也比跟踪 master HEAD 稳。pip 会把 sqlmap 装到 PATH，无需再包一层 wrapper。
RUN pip install --no-cache-dir sqlmap

# ProjectDiscovery 工具：nuclei + httpx（从官方 release 拉二进制，避免装 Go）
# 国内构建优先 ghfast / ghproxy，失败再直连 GitHub。zip 无效则失败，避免镜像 silently 缺工具。
# TARGETARCH 由 buildkit 自动注入(arm64/amd64)
ARG TARGETARCH
RUN set -eux; \
    NUCLEI_VER=3.3.7; HTTPX_VER=1.6.9; \
    cd /tmp; \
    apt-get update && apt-get install -y --no-install-recommends unzip; \
    fetch_zip() { \
      dest="$1"; shift; \
      for u in "$@"; do \
        echo "GET $u"; \
        if wget -q -T 45 -O "$dest" "$u" && unzip -tq "$dest" >/dev/null 2>&1; then \
          return 0; \
        fi; \
        rm -f "$dest"; \
      done; \
      echo "ERROR: could not download valid $dest" >&2; \
      return 1; \
    }; \
    fetch_zip nuclei.zip \
      "https://ghfast.top/https://github.com/projectdiscovery/nuclei/releases/download/v${NUCLEI_VER}/nuclei_${NUCLEI_VER}_linux_${TARGETARCH}.zip" \
      "https://ghproxy.net/https://github.com/projectdiscovery/nuclei/releases/download/v${NUCLEI_VER}/nuclei_${NUCLEI_VER}_linux_${TARGETARCH}.zip" \
      "https://github.com/projectdiscovery/nuclei/releases/download/v${NUCLEI_VER}/nuclei_${NUCLEI_VER}_linux_${TARGETARCH}.zip"; \
    fetch_zip httpx.zip \
      "https://ghfast.top/https://github.com/projectdiscovery/httpx/releases/download/v${HTTPX_VER}/httpx_${HTTPX_VER}_linux_${TARGETARCH}.zip" \
      "https://ghproxy.net/https://github.com/projectdiscovery/httpx/releases/download/v${HTTPX_VER}/httpx_${HTTPX_VER}_linux_${TARGETARCH}.zip" \
      "https://github.com/projectdiscovery/httpx/releases/download/v${HTTPX_VER}/httpx_${HTTPX_VER}_linux_${TARGETARCH}.zip"; \
    unzip -o nuclei.zip nuclei -d /usr/local/bin/; \
    unzip -o httpx.zip httpx -d /usr/local/bin/; \
    chmod +x /usr/local/bin/nuclei /usr/local/bin/httpx; \
    mv /usr/local/bin/httpx /usr/local/bin/httpx.bin; \
    printf '%s\n' \
      '#!/bin/sh' \
      'UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"' \
      'for a in "$@"; do' \
      '  case "$a" in' \
      '    *User-Agent*|*user-agent*) exec /usr/local/bin/httpx.bin "$@" ;;' \
      '  esac' \
      'done' \
      'exec /usr/local/bin/httpx.bin -H "User-Agent: $UA" "$@"' \
      > /usr/local/bin/httpx; \
    chmod +x /usr/local/bin/httpx; \
    rm -f /tmp/*.zip; \
    apt-get purge -y unzip; rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ===== 3.1 新增：Playwright + Chromium（运行时接口收割）=====
# 用途：swagger 被禁时，用真实浏览器录前端实际发出的 XHR，补出 /api/pool/* 这类隐藏业务线。
# 注意：playwright 是官方包，自带独立驱动，不会像 pyppeteer 那样降级 websockets。
# 只装 chromium（不装 firefox/webkit），并清掉缓存控制镜像体积。
#
# 踩坑：python:3.12-slim 缺 libatomic.so.1，playwright 自带的 node 驱动直接 exit 127。
# `playwright install --with-deps` 自己装的依赖不含 libatomic，必须先 apt 补齐。
# 踩坑2：直连 Google 的 chromium 下载源在国内基本卡死，用 playwright 官方支持的重定向：
#        PLAYWRIGHT_DOWNLOAD_HOST 指向 npmmirror 的镜像。
ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright \
    PLAYWRIGHT_SKIP_BROWSER_GC=1 \
    PLAYWRIGHT_DOWNLOAD_HOST=https://cdn.npmmirror.com/binaries/playwright
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libatomic1 libnss3 libnspr4 libatk1.0-0 libatk-bridge2.0-0 \
        libcups2 libdrm2 libxkbcommon0 libxcomposite1 libxdamage1 \
        libxfixes3 libxrandr2 libgbm1 libpango-1.0-0 libcairo2 \
        libasound2t64 libatspi2.0-0 fonts-liberation \
        xvfb dbus-x11 && \
    rm -rf /var/lib/apt/lists/* || \
    (apt-get install -y --no-install-recommends libasound2 xvfb && rm -rf /var/lib/apt/lists/*)
RUN pip install --no-cache-dir "playwright>=1.40,<2" && \
    mkdir -p /ms-playwright && \
    (python -m playwright install chromium || \
     PLAYWRIGHT_DOWNLOAD_HOST=https://npmmirror.com/mirrors/playwright python -m playwright install chromium) && \
    rm -rf /var/lib/apt/lists/* /root/.cache/pip

# 修复：requirements.txt 里的 httpx[socks] 是 Python 库，pip 会覆盖 /usr/local/bin/httpx
# （ProjectDiscovery 的二进制此时已被改名为 httpx.bin）。这里重写 wrapper，
# 保证镜像重建后 httpx 仍是 PD 命令行工具。
RUN printf '%s\n' \
      '#!/bin/sh' \
      'UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"' \
      'for a in "$@"; do' \
      '  case "$a" in' \
      '    *User-Agent*|*user-agent*) exec /usr/local/bin/httpx.bin "$@" ;;' \
      '  esac' \
      'done' \
      'exec /usr/local/bin/httpx.bin -H "User-Agent: $UA" "$@"' \
      > /usr/local/bin/httpx \
    && chmod +x /usr/local/bin/httpx

# 更新 nuclei 模板（失败不阻断构建）
RUN nuclei -update-templates -silent || true

COPY . .
# Windows 检出/解压可能带 CRLF；入口脚本带 \r 时容器会报 no such file or directory。
RUN find /app/scripts -type f -name '*.sh' -exec sed -i 's/\r$//' {} +

# 拷入前端构建产物（覆盖空的 web/dist）
COPY --from=frontend /web/dist /app/web/dist

# 工作区 + 数据目录（数据目录建议挂卷持久化）
RUN mkdir -p /work /app/data
ENV WORKER_WORK_ROOT=/work \
    DB_PATH=/app/data/autohunter.db

EXPOSE 18800

CMD ["sh", "/app/scripts/run-with-watchdog.sh"]
