#!/usr/bin/env python

# task: delete k-th element counting from the end of list

from mynode import *
import unittest
import logging
import sys
import re

if len(sys.argv) > 1:
    loglevel = sys.argv[1]
    loglevel = re.split('=', loglevel)[1] # ok, I know it's ugly, but I couldn't make getopt work, so I hated it
    logging.basicConfig(level=loglevel)
#logging.warning('whoa')
logging.info('info!')

def delete_k_from_end(k,ll):
    if k == 0 or ll is None:
        raise IndexError
    ptr1, ptr2 = ll, ll

    for i in range(k):
        ptr2 = ptr2.next_node
        if ptr2 is None and i != k-1:
            raise IndexError

    prev = None
    while ptr2 is not None:
        prev = ptr1
        ptr1 = ptr1.next_node
        ptr2 = ptr2.next_node
    # ptr2 at the end, ptr1 needs to be deleted

    if prev is not None:
        prev.next_node = ptr1.next_node
        return ll
    else:
        return ptr1.next_node

class MyTest(unittest.TestCase):
    def test_empty(self):
        self.assertRaises(IndexError, delete_k_from_end, 0, from_array([]))
        self.assertRaises(IndexError, delete_k_from_end, 2, from_array([]))
        self.assertRaises(IndexError, delete_k_from_end, 0, from_array([1,2]))

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
        self.assertRaises(IndexError, delete_k_from_end, 5, ll)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
