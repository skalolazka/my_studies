#!/usr/bin/env python
import sys
# takes 64-bit int, returns int, consisting of bits of that int in reverse

def reverse (x):
    """
    >>> reverse(0)
    '0'
    >>> reverse(1)
    '1'
    >>> reverse(2) # 10
    '01'
    >>> reverse(3) # 11
    '11'
    >>> reverse(6) # 110
    '011'
    >>> reverse(13) # 1101
    '1011'
    >>> reverse(57) # 111001
    '100111'
    >>>
    """
#    print "binary x: %s" % (bin(x))
    result = []
    if not x:
        return '0'
    while x:
        end = x & 1
        result.append(end)
        x >>= 1
    string = ''
    for val in result:
        string = string + str(val)
    return string

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = False, optionflags= doctest.REPORT_ONLY_FIRST_FAILURE)
    #result = reverse(int(sys.argv[1]))
