# Forensics II

## Assignment details

This assignment has one part. It is due by 3/15/18 at 11:59PM. To submit your work, please post
either a public note **or** a link to your publicly available writeup on Piazza.

**There will be a late penalty of 5% per day late!**

### Part 1

In this part, you are tasked with writing a parser for a novel binary format:
[FPFF](https://github.com/UMD-CSEC/fpff). You can find the FPFF spec
[here](https://github.com/UMD-CSEC/fpff/blob/master/spec/fpff_spec.pdf). You will then use
your parser to analyze a FPFF file ([foo.fpff](foo.fpff)), and report the information you find
within it.

Perform the following tasks:

1. Develop the parser, using both the
[specification](https://github.com/UMD-CSEC/fpff/blob/master/spec/fpff_spec.pdf) and
`foo.fpff` for reference. [`stub.py`](stub.py) contains the beginnings of a Python parser, if
you'd like to develop in Python (2).

2. Parse `foo.fpff`, and report the following information:
    1. When was `foo.fpff` generated?
    2. Who authored `foo.fpff`?
    3. How many sections does `foo.fpff` *say* it has? How many sections are there *really*?
    4. List each section, giving us the data in it *and* its type.
    5. Report the two flags hidden in `foo.fpff`, and the one flag on the web referenced by
    `foo.fpff`.

#### Important notes

1. Make sure to submit **all** of the code you write, even if based on `stub.py`!
2. Don't worry about implementing 100% of the specification. Your parser will only be tested on
`foo.fpff`, and any section types that do not appear in `foo.fpff` will not be tested for.

### Scoring

Part 1 is worth 100 points, broken down between the parser (50 points) and analysis (50 points).

### Tips

Remember to document your steps for maximum credit!

Look at the Forensics I and II slides for guidance.

If you're using Python, Ruby, or another scripting language, check out the `pack` and `unpack`
methods:

* Python 2 - [`struct`](https://docs.python.org/2/library/struct.html)
* Python 3 - [`struct`](https://docs.python.org/3.5/library/struct.html)
* Ruby - [`Array#pack`](https://ruby-doc.org/core-2.5.0/Array.html#method-i-pack) and
[`String#unpack`](https://ruby-doc.org/core-2.5.0/String.html#method-i-unpack)
