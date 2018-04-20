global _start
section .text

_start:
  mov eax, 4
  mov ebx, 1
  mov ecx, hello
  mov edx, 12
  int 80h

  mov eax, 1
  mov ebx, 0
  int 80h

section .data

hello:
  db "Hello there", 0ah
