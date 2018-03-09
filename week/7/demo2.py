#!/usr/bin/env python2

import sys
import struct
from datetime import datetime

MAGIC = 0x13371337

data = sys.stdin.read()

magic, timestamp, nbytes = struct.unpack("<LLL", data[0:12])

print("Magic: %s" % hex(magic))
print("Timestamp: %d (%s)" % (timestamp, datetime.fromtimestamp(timestamp)))
print("# of bytes in string: %d" % nbytes)

string = struct.unpack("%ds" % nbytes, data[12:12+nbytes])
print("string: %s" % string)

