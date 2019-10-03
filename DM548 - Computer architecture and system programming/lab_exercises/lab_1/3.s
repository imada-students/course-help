.section .data
.section .text
.globl _start

_start:
	movq $1, %rax			# Reset RAX ( Accumulator )
	movq $1, %rcx			# Reset RCX ( Counter )	

# Loop to sum numbers
multiloop:
	imulq %rcx, %rax		# Add counter variable to RAX
	incq %rcx				# Increment counter

	cmp $9, %rcx			# Check counter against value 9
	jle multiloop		    # Jump to end if RCX greater or equal to 9

end:
	call print_rax            # print the RAX register
	# Syscall exit
	movq $60, %rax            # rax: int syscall number
	movq $0, %rdi             # rdi: int error code
	syscall


# Prints the contents of rax.
.type print_rax, @function   # This is for debugging
print_rax:
	# function prolog
	push %rbp
	movq %rsp, %rbp

	# saving registers the registers on the stack
	push %rax
	push %rcx
	push %rdx
	push %rdi
	push %rsi
	push %r9

	movq $6, %r9           # we always print the 6 characters "RAX: \n"
	push $10               # put '\n' on the stack

loop1:
	movq $0, %rdx
	movq $10, %rcx
	idivq %rcx             # idiv alwas divides rdx:rax/operand
						   # result is in rax, remainder in rdx
	addq $48, %rdx         # add 48 to remainder to get corresponding ASCII
	push %rdx              # save our first ASCII char on the stack
	addq $1, %r9           # counter
	# loop until rax = 0
	cmpq $0, %rax   
	jne loop1

	# and then push the prefix of our output
	movq $0x20, %rax       # ' '
	push %rax
	movq $0x3a, %rax       # ':'
	push %rax
	movq $0x58, %rax       # 'X'
	push %rax
	movq $0x41, %rax       # 'A"
	push %rax
	movq $0x52, %rax       # 'R'
	push %rax

print_loop:
	movq $1, %rax          # Here we make a syscall. 1 in rax designates a sys_write
	movq $1, %rdi          # rdx: int file descriptor (1 is stdout)
	movq %rsp, %rsi        # rsi: char* buffer (rsp points to the current char to write)
	movq $1, %rdx          # rdx: size_t count (we write one char at a time)
	syscall                # instruction making the syscall
	addq $8, %rsp          # set stack pointer to next char
	addq $-1, %r9
	jne print_loop

	# restore the previously saved registers
	pop %r9
	pop %rsi
	pop %rdi
	pop %rdx
	pop %rcx
	pop %rax

	# function epilog
	movq %rbp, %rsp
	pop %rbp
	ret