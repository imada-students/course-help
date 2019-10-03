.section .data

    # String from exercise
	_str: .string "Hello World!\n"

.section .text
.globl _start

_start:
	
    movq $0, %rbx           # Reset
    movq (%rsp), %r8          # Stack pointer register contains number of arguments
    movq 8(%rsp), %r9       # Pointer to beginning of string in memory

    # General idea, add 8 to pointer, and subract 1 from r8. When number of arguments reaches 0, stop

    _argloopstart:

        # Read the argument and write it continously, character for character. When the null character is reached, exit loop

        movq %r9, %r10 # r10 is zPointer to character in memory, is incremented by 1 when a char is read

        _charloopstart:
            # Put current char into %rbx (lower portion)
            movq $0, %rbx
            movb (%r10), %bl

            # Check if character is null - if it is, go to loop end, otherwise, print and proceed
            cmp $0, %rbx			# Compare char to null character
            je _charloopend

            # Print character in rbxf
            movq $1, %rax			# Write syscall
            movq $1, %rdi			# Write to stdout
            movq %rbx, %rsi  		# Character to write put in rbx
            movq $1, %rdx			# Length of string to write in rdx
            syscall

            # Loop endCharacter to write put in rbx
            inc %r10 # Next character
            jmp _charloopstart

        _charloopend:

    # Loop end
    add $8, %r9         # Point to next argument reference in stack
    dec %r8             # 1 fewer argument

    # Print new line character after each argument
    movq $1, %rax			# Write syscall
    movq $1, %rdi			# Write to stdout
    movq $0x0a, %rsi  		# Write newline character (0x0A)
    movq $1, %rdx			# Length of string to write in rdx
    syscall

    # Check whether r8 has reached 0. If it has, exit loop, exiting program, otherwise restart loop
    cmp $0, %r8
    jne _argloopstart

    _argloopend:

	# Syscall exit
	movq $60, %rax			# rax: int syscall number
	movq $0, %rdi			# rdi: int error code
	syscall
