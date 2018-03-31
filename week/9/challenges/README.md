# Crypto I

## Assignment details

This assignment has two parts. It is due by 4/5/18 at 11:59PM. To submit your work, please post
either a public note **or** a link to your publicly available writeup on Piazza.

**There will be a late penalty of 5% per day late!**

### Part 1

You have successfully infiltrated one of the servers at Briong, and have
extracted an `/etc/shadow` file! Use what you've learned so far to answer the
following questions:

  1. What is the hashing algorithm(s) used to secure these passwords?
  2. What salt is used for these passwords, if any?
  3. When were the passwords changed, if at all?
  4. What are the restrictions each user has on changing their password, if any?
  5. Have any passwords expired? If so, whose?
  6. Use one of the tools discussed in class (hashcat, JohnTheRipper) to try and
  recover each password and show how you used the tool.

### Part 2

You have also found various hashes laying around on the server. From the notes
you have gathered during your penetration testing, you think that they are
passwords picked from this [password list](https://github.com/danielmiessler/SecLists/blob/master/Passwords/darkweb2017-top1000.txt).
You also found out that these passwords are *salted* with a single lowercase
letter (a, b, c, ..., z) prepended to each password before being hashed with the
*SHA512 algorithm*, though you don't know if the same salt is used for each
password. Your task is to try and manually break these hashes with a sort of
custom rainbow table and recover the passwords and the salts. Use your Python-fu
to crack these hashes, providing both the *salt* and the *password* for each
hash. Stub code is provided in [part2.py](part2.py).

### Part 3

You stumbled upon a hidden service not discovered by your port scans. It seems
like one of Briong's interns desperately needs a calculator for his Algebra
homework. He's fairly good at mental math, but not good enough -- try and write
a script to do his homework faster than he can, and he might give you a flag for
your help. `nc irc.csec.umiacs.umd.edu 4444` (Stub code is in
[part3.py](part3.py)) Submit the flag you get in return.

#### Important notes

Make sure to submit **all** of the code you write, even if based on the stub
code! You will need to submit your code for both Part 2 and Part 3.

### Scoring

* Part 1 is worth 30 points
* Part 2 is worth 35 points
* Part 3 is worth 35 points

### Tips

Remember to document your thought process for maximum credit!

Review the slides for help with using any of the tools or libraries discussed in
class, as well as consult the `man` pages for any of the tools discussed and for
the `shadow` file format and the hash format (shadow(5) and crypt(3))

Look back at your Homework 2 code if you need a refresher on working with
sockets for Part 3.

Pro tip: along with the online Python references, you can also open up an
interactive Python session (by typing `python` in your shell) and import the
module of choice (e.g. `import sys`) and call `help()` on that module
(e.g. `help(sys)`) to get a `man`page-like reference to how to use that module!

* Python 2 - [`hashlib`](https://docs.python.org/2/library/hashlib.html)
* Python 2 - [`socket`](https://docs.python.org/2/library/socket.html)
* Python 3 - [`hashlib`](https://docs.python.org/3.5/library/hashlib.html)
* Python 3 - [`socket`](https://docs.python.org/3.5/library/socket.html)
