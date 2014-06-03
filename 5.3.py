#!/usr/bin/env python
import sys
# takes 64-bit int, returns int, consisting of bits of that int in reverse

def reverse (x):
    """
    >>> reverse(0)
    0
    >>> reverse(1)
    1000000000000000000000000000000000000000000000000000000000000000L
    >>> reverse(2) # 10
    100000000000000000000000000000000000000000000000000000000000000L
    >>> reverse(3) # 11
    1100000000000000000000000000000000000000000000000000000000000000L
    >>> reverse(6) # 110
    110000000000000000000000000000000000000000000000000000000000000L
    >>> reverse(13) # 1101
    1011000000000000000000000000000000000000000000000000000000000000L
    >>> reverse(57) # 111001
    1001110000000000000000000000000000000000000000000000000000000000L
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
    return int(string)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = False, optionflags= doctest.REPORT_ONLY_FIRST_FAILURE)
    #result = reverse(int(sys.argv[1]))
    #print result
