# Binaries I

## Assignment details

This assignment has two parts. It is due by 4/26/18 at 11:59PM. To submit your work, please post
either a public note **or** a link to your publicly available writeup on Piazza.

**There will be a late penalty of 5% per day late!**

### Part 1

You are given two subroutines written in x86 assembly. Your task is to reverse
engineer both of them to figure out what they are trying to accomplish. The main
goal for each of them is listed as a comment in both files. Your submission
should include a qualitative description of what subroutines are doing.
Depending on how you came across your answers, please provide any supporting
materials that show your understanding of the code snippets. 

For example, if you trace them by hand, show pictures/screenshots of any
calculations or stack traces along with your explanation. If you manage to compile
these functions into a larger program that executes it, then use `gdb` to step
through the instructions, then provide screenshots of your `gdb` showing the
different instructions and how they manipulate the stack. You can type
`set disassembly-flavor intel` into `gdb` to use Intel disassembly syntax.

The two snippets are located in [re1.s](challenges/re1.s) and [re2.s](challenges/re2.s)

### Part 2

Here you will be exercising your shellcoding-foo!

Write a function in x86 assembly 32-bit mode with the label `tribonacci` that
computes the Tribonacci sequence. The sequence is defined as:

```
T(0) = 0
T(1) = 1
T(2) = 1
T(n) = T(n-1) + T(n-2) + T(n-3)
```

Your function will take some reasonable number `n` as input and will return `T(n)`.

You don't need to worry about values that are too large to fit in the 32-bit
`eax` return register, so long as any value smaller than 32 bits are returned
properly.

Make sure to use proper callee-saving conventions as mentioned in the lecture
notes. Use whatever techniques you learned from lecture or from CMSC216 to help
you properly calculate the value in the sequence.

#### Important notes

Make sure to submit **all** of the code you write, even if based on the stub
code! Make sure to include anything that lets us know that you understand what
is going on when reverse engineering!

We will only be able to provide support with this assignment if you are using the VM!
Any other means or methods of solving these challenges will not receive help if
they are being done on your native machines (even if you're running a flavor of Linux!)

### Scoring

* Part 1 is worth 60 points
* Part 2 is worth 40 points

### Tips

Remember to document your thought process for maximum credit!

Review the slides for reference with using any of the tools, instructions, or
tables discussed in class.
