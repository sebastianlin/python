#!/usr/bin/python
#-*- coding: utf-8 -*-

import os, sys, zlib

def crc32_calculation(filename):
    try:
        blocksize = 1024 * 64
        fd = open(filename, "rb")
        content = fd.read(blocksize)
        checksum = 0
        while len(content) != 0:
            checksum = zlib.crc32(content, checksum) & 0xFFFFFFFF
            content = fd.read(blocksize)
        fd.close()

    except:
        sys.exit('Error: CRC32 Calculation Failed')

    return checksum

if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit('Usage: %s {filename}' % os.path.basename(sys.argv[0]))

    if not os.path.exists(sys.argv[1]):
        sys.exit('Error: File Not Exist or Access Denied')

    result = crc32_calculation(sys.argv[1])

    print '%08X %s' % (result, os.path.basename(sys.argv[1]))

