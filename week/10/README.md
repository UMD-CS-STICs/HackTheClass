# Crypto II

## Assignment details

This assignment has two parts. It is due by 4/15/18 at 11:59PM. To submit your work, please post
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
length yourself. Use the [stub.py](challenges/stub.py) code to help you craft a valid signature
on a custom payload. The notary lives on `159.89.236.106:5678`. Thus, you may connect to the challenge over nc using: `$ nc 159.89.236.106 5678`.

### Part 2

Send us an encrypted email using this [PGP public key](challenges/pgpassignment.key) to `pgpassignment@gmail.com`. The body of the email should be formatted as such:

```
Message

Your PGP public key
```

For example:

```
-----BEGIN PGP MESSAGE-----

hQEMA5H4hkZSunZWAQf+PHS12Pi6U/lrKnkysNgiThnclRown2YwLH2cZ4AAB/uW
...
SqSKFAsbViMw6dd0tfY6Ssz5Jteb0imV/h4nNQ3eRO6aiyg=
=CRCE
-----END PGP MESSAGE-----

-----BEGIN PGP PUBLIC KEY BLOCK-----

mQENBFrMIqgBCADwQGU9JzZBiPqPzW6z58gW03ywxwr+IWBS8G+D0eH3xHPwqahL
...
rOVihu+kweme13cUB4TdymIyjiU+fFACycql1kgsy8w2Tk
TNkRlxITrW5DdYxOdKEqyQ8idHAu+YKTgus9Ab0elw==
=T1aV
-----END PGP PUBLIC KEY BLOCK-----

```

If we are able to decrypt your message, then we will send you an email back which will be encrypted with your public key. If you are successfully able to decrypt the message, then you will get a flag. 

In your writeup, show us the commands you used to do this. We suggest trying this assignment using two keys you control (sending yourself PGP encrypted emails using different PGP keys) and then testing it with us. You may choose to send us a signed message or not.


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
