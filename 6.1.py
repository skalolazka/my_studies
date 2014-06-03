#!/usr/bin/env python
import sys
# takes array and i, rearranges array - first elements < array[i],
# then equal, then greater

def rearrange (arr, i):
    """
    >>> rearrange([0], 0)
    [0]
    >>> rearrange([0, 1], 0)
    [0, 1]
    >>> rearrange([0, 1], 1)
    [0, 1]
    >>> rearrange([0, 1, 0], 0)
    [0, 0, 1]
    >>>
    >>> rearrange([0, 1, 2, 0, 2, 1, 0], 1)
    [0, 0, 0, 1, 1, 2, 2]
    >>> rearrange([2, 2, 0, 0], 1)
    [0, 0, 2, 2]
    """
    pivot = arr[i]
    middle_index = 0
    big_index = 0
    for j in range(len(arr)):
#        print 'start '+str(locals())
        if arr[j] < pivot:
#            print '<'
            (arr[j], arr[middle_index]) = (arr[middle_index], arr[j])
            (arr[j], arr[big_index]) = (arr[big_index], arr[j])
            middle_index += 1
            big_index += 1
        elif arr[j] == pivot:
#            print '=='
            (arr[j], arr[big_index]) = (arr[big_index], arr[j])
            big_index += 1
#        else: # arr[j] > pivot
#            print '>'
#        print 'end '+str(locals())
    return arr

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = False, optionflags= doctest.REPORT_ONLY_FIRST_FAILURE)
#    print rearrange([0, 2, 1, 0, 1, 2, 3], 2)
