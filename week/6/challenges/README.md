# Forensics I

## Assignment details

This assignment has three parts. It is due by 3/8/18 at 11:59 PM. To submit your work, please post
either a public note **or** a link to your publicly available writeup on Piazza.

**There will be a late penalty of 5% per day late!**

### Setup

You may find `exiftool` and `steghide` useful for parts of this assignment. Installing them
is straightforward:

```bash
$ sudo apt install exiftool steghide
```

### Part 1

The `imagefun.jpg` file is a [JPEG image](https://en.wikipedia.org/wiki/JPEG). In this part,
your job is to investigate its metadata:

1. What kind of device took the photo? What specifics can you ascertain about it (the device), and
why might they be relevant?
2. When and where was the photo taken? Why might this be relevant?
3. Find the two flags hidden in the photo.

### Part 2

The `fubar.core` file contains a [core dump](https://en.wikipedia.org/wiki/Core_dump) from a
running program. In this part, your job is to discover information about the program at runtime:

1. What kind of system was the program built for? (e.g., OS, libc version, compiler version)
2. What arguments was the program run with?
3. What was in the program's environment when it was dumped?
4. What other data is embedded in the program?

### Part 3

The `traffic.pcap` file contains a record of some traffic collected by one of the Briong company's
firewalls. In this part, your job is to analyze the traffic and reconstruct the visited website:

1. What was the domain requested in the HTTP request, and what IP did it resolve to?
2. What was the relative URL of the page that was requested?
3. Reconstruct the page (including images) and take a screenshot of it.
4. Find the flag (there's only one!)
5. What other connections/protocols are in the packet capture? Pick one, and explain why it
might be interesting.

### Format

All three parts should be written in the same (blog) post, clearly separated.

For each component, make sure to give the answer **and** an explanation of how you found the
answer.

### Scoring

Part 1 is worth 40 points, and parts 2 and 3 are worth 30 each.

### Tips

Remember to document your steps!

Look at the Forensics I slides for guidance.

Look at the manpages when in doubt, e.g. `man exiftool`.

Good luck!
