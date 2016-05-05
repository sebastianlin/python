#!/usr/bin/python


"""
Use "Struct" module to extract binary data from a file.
"""


import struct

# pack
str1 = struct.pack("bbbbbbbb", 0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x0A)
print("Struct Pack function:" + str1)

file = open("tmpfile",  'w+')
file.write(str1);
file.seek(0)

# calcsize
str2 = file.read(struct.calcsize("bbbbbbbb"))
print("Readback str from file:" + str2)

# unpack
str3 = struct.unpack("bbbbbbbb", str2)
print("Struct UnPack function:" + str(str3))



