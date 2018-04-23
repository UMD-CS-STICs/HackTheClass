; what does this return?
section .text
do_this:
  push ebp
  mov ebp, esp
  push edi

  mov al, 33h
  mov cl, 4
  lea edi, [x]

  rep stosb

  xor BYTE [x], 0
  xor BYTE [x+1], 0bh
  xor BYTE [x+2], 0ah
  xor BYTE [x+3], 61h

  mov eax, [x]

  pop edi
  mov esp, ebp
  pop ebp
  ret

section .data
x dd 0
