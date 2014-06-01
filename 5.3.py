#!/usr/bin/env python
import sys
# takes 64-bit int, returns int, consisting of bits of that int in reverse

def reverse (x):
    """
    >>> reverse(0)
    '0000000000000000000000000000000000000000000000000000000000000000'
    >>> reverse(1)
    '1000000000000000000000000000000000000000000000000000000000000000'
    >>> reverse(2) # 10
    '0100000000000000000000000000000000000000000000000000000000000000'
    >>> reverse(3) # 11
    '1100000000000000000000000000000000000000000000000000000000000000'
    >>> reverse(6) # 110
    '0110000000000000000000000000000000000000000000000000000000000000'
    >>> reverse(13) # 1101
    '1011000000000000000000000000000000000000000000000000000000000000'
    >>> reverse(57) # 111001
    '1001110000000000000000000000000000000000000000000000000000000000'
    >>>
    """
#    print "binary x: %s" % (bin(x))
    i = 0
    result = [0 for k in range(64)]
    while i < 64:
        tmp = x & 1
        result[i] = tmp
        x >>= 1
	i += 1
#	print locals()
    string = ''
    for val in result:
        string = string + str(val)
    return string

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = False, optionflags= doctest.REPORT_ONLY_FIRST_FAILURE)
    #result = reverse(int(sys.argv[1]))
    #print result
