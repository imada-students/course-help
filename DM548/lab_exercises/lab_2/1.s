.section .data
.section .text
.globl _start

_start:
	movq $42, %rdi
    call printNum

    # Syscall exit
	movq $60, %rax            # rax: int syscall number
	movq $0, %rdi             # rdi: int error code
	syscall

	