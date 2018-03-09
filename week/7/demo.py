#!/usr/bin/env python2

import sys
import struct
from datetime import datetime

MAGIC = 0x13371337

data = sys.stdin.read()
i = 0

# note the comma here! struct.unpack returns a tuple.
magic, = struct.unpack("<L", data[i:4])

# we've read the first 4 bytes, so move up in the stream by 4 bytes
i += 4

print("Magic: %s" % hex(magic))

timestamp, = struct.unpack("<L", data[i:i+4])
i += 4

print("Timestamp: %d (%s)" % (timestamp, datetime.fromtimestamp(timestamp)))

nbytes, = struct.unpack("<L", data[i:i+4])
i += 4

print("# of bytes in string: %d" % nbytes)

string = struct.unpack("%ds" % nbytes, data[i:i+nbytes])
print("string: %s" % string)

# string = data[i:i+nbytes]
# print("string: %s" % string)
