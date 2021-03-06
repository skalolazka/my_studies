#!/usr/bin/env python
import sys

def parity (x):
    r = 0
#    print "binary x: %s" % (bin(x))
    while x:
        r ^= (x & 1)
        x >>= 1
#        print "r: %s, x: %s" % (r, bin(x))
    return r

if __name__ == '__main__':
    result = parity(int(sys.argv[1]))
    if result:
        print "%s is even" % (sys.argv[1])
    else:
        print "%s is odd" % (sys.argv[1])
