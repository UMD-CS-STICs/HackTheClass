; what does this return?
section .text
do_this:
  push ebp
  mov ebp, esp

  mov ecx, 4
  mov dl, 0ffh

f:
  shl eax, 8
  or al, dl
  loop f

  mov ecx, 8
  mov dx, 6761h
  shl edx, cl
  shl edx, cl
  mov dx, 6c66h

  xor eax, edx
  not eax

  mov esp, ebp
  pop ebp
  ret
