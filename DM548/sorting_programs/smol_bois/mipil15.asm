.section .data
	file_stat:	.space 144	#; Size of the fstat struct

#; Strategy:
#; Get file descriptor from input
#; Allocate memory for whole file
#; Read file into that memory
#; count newlines
#; Allocate memory for newlines * number sizes (in chars)
#; copy file with padding into allocated memory region
#; Sort using gnome sort and string instructions
#; write memory using  to stdout

.section .text
.global _start
_start:
	#; Get the 1. command line argument
	mov 16(%rsp), %rdi
	
	#; Get file descriptor
	mov $2, %rax		#Open file
	xor %esi, %esi
	xor %edx, %edx
	syscall
	
	mov %rax, %r13
	#; %r13 contains file descriptor
	
	#; Get size of file
	mov $5, %rax
	mov %r13, %rdi
	mov $file_stat, %rsi
	syscall
	mov $file_stat, %rax
	mov 48(%rax), %r14
	
	#; %r14 now contains file size
	
	#; Allocate enough room for the whole file
	xor %rdi, %rdi
	mov $12, %rax
	syscall 			#; %rax now contains end of heap
	mov %rax, %r12		#; Save the beginning of the new buffer
	add %r14, %rax		#; Calculate the addition of the extra space
	mov %rax, %rdi
	mov $12, %rax
	syscall
	
	#; Read max 200 bytes from file
	mov %r13, %rdi		#; From file
	mov $0, %rax		#; read
	mov %r14, %rdx		#; size of the file
	mov %r12, %rsi		#; to the buffer
	syscall

	#; Write to stdout
	mov %r14, %rdx		#; Bytes to write
	mov $1, %rax		#; Syscall: Write
	mov $1, %rdi		#; File descriptor: stdout
	mov %r12, %rsi		#; Address of buffer
	syscall

	mov $60, %rax		#; Syscall: exit
	mov $0, %rdi		#; Return code success
	syscall

