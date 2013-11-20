#!/usr/bin/env python

import sys

def mapper(argv):
    idx = 0
    for line in sys.stdin:
        clean_line = line.strip()
        if idx < 100:
            print clean_line
            idx += 1

if __name__ == "__main__":
    mapper(sys.argv)
