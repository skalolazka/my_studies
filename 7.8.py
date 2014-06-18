#!/usr/bin/env python

from mynode import *

def delete_k_from_end(k,ll):
    if k == 0:
        return None
    if ll is None:
        return None
    ptr1, ptr2, first = ll, ll, ll

    for i in range(k-1):
        print 'i ', i
        ptr2 = ptr2.next_node
        if ptr2 is None:
            return 0

    prev = None
    while ptr2.next_node is not None:
        print 'go'
        prev = ptr1
        ptr1 = ptr1.next_node
        ptr2 = ptr2.next_node
        print 'val1 ', ptr1.value, 'val2 ', ptr2.value
    # ptr2 at the end, ptr1 needs to be deleted

#    print 'prev ', prev.value, 'ptr1 ', ptr1.value, 'ptr1.next ', ptr1.next_node
    print 'prev ', prev, 'ptr1 ', ptr1
    if prev is not None:
        prev.next_node = ptr1.next_node
        return first
    elif ptr1.next_node is not None:
        prev = ptr1.next_node
        return ptr1.next_node
    else:
        return None


import unittest

class MyTest(unittest.TestCase):
    def test_empty(self):
        res = delete_k_from_end(0, from_array([]))
        self.assertEqual(res, None, 'empty')
        res = delete_k_from_end(2, from_array([]))
        self.assertEqual(res, None, 'empty')
        res = delete_k_from_end(0, from_array([1,2]))
        self.assertEqual(res, None, 'empty')

    def test_long(self):
        ll = from_array([1,2,3])
        ll = delete_k_from_end(1, ll)
        self.assertEqual(to_array(ll), [1,2], 'last really deleted')
        ll = delete_k_from_end(1, ll)
        self.assertEqual(to_array(ll), [1], 'one left now')
        ll = delete_k_from_end(1, ll)
        self.assertEqual(to_array(ll), [], 'none left now')
        ll = from_array([2,3,4])
        ll = delete_k_from_end(2, ll)
        self.assertEqual(to_array(ll), [2,4], 'middle one really deleted')
        ll = from_array([2,3,4])
        ll = delete_k_from_end(3, ll)
        self.assertEqual(to_array(ll), [3,4], 'really deleted')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
