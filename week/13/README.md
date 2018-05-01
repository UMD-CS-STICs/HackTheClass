# Binaries II

## Assignment details

This assignment has two parts. It is due by 5/7/18 at 11:59PM. To submit your work, please post
either a public note **or** a link to your publicly available writeup on Piazza.

**There will be a late penalty of 5% per day late!**

### Part 1

You are given two programs written in C. Your task is to reverse
engineer both of them to figure out what they are doing, and find the flags in
each of them. The flag is in the format `389R-{flag_text_goes_here}`.

Your writeup should include a brief description of what the two programs do,
as well as your thought process as you went from start to solve for these
programs.

The two binaries are located in [stackexchange](challenges/stackexchange) and
[onebyone](challenges/onebyone).

### Part 2

You are trying to access a restricted resource on the Briong server, which uses
a vulnerable password checker. Luckily, you have someone on the inside that has
leaked the source code for the checker. Scan through the code to see if you can
break in. `nc 167.99.224.34 9998`. [outofbounds.c](challenges/outofbounds.c)

Your writeup should include a brief description of what the program does,
what might be going wrong with the program, how you utilized this vulnerability,
as well as other thought processes as you went from start to solve for these
programs.

### Scoring

* Part 1 is worth 60 points
* Part 2 is worth 40 points

### Tips

Remember to document your thought process for maximum credit!

Review the slides for reference with using any of the tools, instructions, or
tables discussed in class. You may find help with `radare2` with the visual
graph (with `VV` from the r2 shell) or with any of the `gdb` plugins mentioned in class.
