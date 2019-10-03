.section .data

    # String from exercise
	_str: .string "Hello World!\n"

.section .text
.globl _start

_start:
	# Write your solution code here
	movq $0, %r8			# Counter register
	movq $0, %rbx			# Current byte to compare
	movq $0, %r10			# Contains memory address to read from

	_loopstart:
		# Idea: Compare current byte of string to null string - if it is, exit loop, else begin loop

		# Calculate memory address
		movq $_str, %r10
		add %r8, %r10

		# Loop logic
		inc %r8				# Increment counter
		
		movb (%r10), %bl		# Put content of what r10 points to byte in r9
		cmp $0, %rbx			# Compare r9 (Byte to compare from string) to 0
		jne _loopstart		# If byte Not Equal to zero, try again

	_loopend:
		# End, load counter in to RDI
		dec %r8				# Decrement counter to counter redundant increment in loop
		movq %r8, %rdi


	call printNum			# prints the RDI register

	# Syscall exit
	movq $60, %rax			# rax: int syscall number
	movq $0, %rdi			# rdi: int error code
	syscall
