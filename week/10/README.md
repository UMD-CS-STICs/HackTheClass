# Crypto II

## Assignment details

This assignment has two parts. It is due by 4/5/18 at 11:59PM. To submit your work, please post
either a public note **or** a link to your publicly available writeup on Piazza.

**There will be a late penalty of 5% per day late!**

### Part 1

You have come across a digital notary who is using MD5 hashing to sign messages.
The notary can either generate a signature for you by prepending your message
with a random secret, or test a signature against a new message. Each time you
request a new signature, he will generate a new secret for your data, but will
keep the same secret for every signature test.

Your task is to show the notary that this signature scheme is vulnerable to a
hash length extension attack. You have heard that the length of the secret he
uses is only 6 bytes (48 bits) long, so you won't need to try and determine this
length yourself. Use the [stub.py](stub.py) code to help you craft a valid signature
on a custom payload. The notary lives on `irc.csec.umiacs.umd.edu 5678`.

### Part 2

#### Important notes

Make sure to submit **all** of the code you write, even if based on the stub
code! You will need to submit your code for Part 1.

### Scoring

* Part 1 is worth 70 points
* Part 2 is worth 30 points

### Tips

Remember to document your thought process for maximum credit!

Review the slides for help with using any of the tools or libraries discussed in
class.
