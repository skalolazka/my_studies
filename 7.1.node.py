#!/usr/bin/env python

from mynode import *

def merge_ll(l1, l2):
    ptr1, ptr2 = l1, l2
    if ptr1 is None:
        return ptr2
    if ptr2 is None:
        return ptr1
    first = None
    while True:
        if ptr1.value > ptr2.value:
            ptr1, ptr2 = ptr2, ptr1
        old_next1, old_next2 = ptr1.next_node, ptr2.next_node
        if ptr1.value <= ptr2.value:
            if first is None:
                first = ptr1
            if old_next1 is None or old_next1.value > ptr2.value:
                ptr1.next_node = ptr2
                if old_next1 is None:
                    break
            ptr1 = old_next1
    return first



import unittest


class MyTest(unittest.TestCase):

    def test_empty(self):
        first = merge_ll(from_array([None]), from_array([None]))
        self.assertIsInstance(first, MyNode, 'class')
        self.assertEqual(first.value, None, 'no value')
        self.assertEqual(first.value, None, 'no next')

        first = merge_ll(from_array([]), from_array([]))
        self.assertEqual(first, None, 'empty')

        first = merge_ll(from_array([0]), from_array([]))
        self.assertEqual(to_array(first), [0], 'one empty, val 0')

        first = merge_ll(from_array([2]), from_array([]))
        self.assertEqual(to_array(first), [2], 'one empty')

        first = merge_ll(None, from_array([3]))
        self.assertEqual(to_array(first), [3], 'first empty')

        first = merge_ll(None, from_array([0]))
        self.assertEqual(to_array(first), [0], 'first empty, val = 0')

    def test_one(self):
        first = merge_ll(from_array([2]), from_array([3]))
        self.assertEqual(to_array(first), [2,3], 'one elem in each')

        first = merge_ll(from_array([3]), from_array([2]))
        self.assertEqual(to_array(first), [2,3], 'first one bigger')

    def test_many(self):
        first = merge_ll(from_array([2,5]), from_array([3]))
        self.assertEqual(to_array(first), [2,3,5], 'two and one in the middle')

        first = merge_ll(from_array([2,5,5]), from_array([3,4,4]))
        self.assertEqual(to_array(first), [2,3,4,4,5,5], 'same values')

        first = merge_ll(from_array([2,5,6,7,8]), from_array([3,4,9,10,11,12,13]))
        self.assertEqual(to_array(first), [2,3,4,5,6,7,8,9,10,11,12,13], 'long=)')

        first = merge_ll(from_array([2,4,6,8]), from_array([3,5,7,9]))
        self.assertEqual(to_array(first), [2,3,4,5,6,7,8,9], 'zig-zag=)')

    def test_one_long(self):
        first = merge_ll(from_array([1,2,3]), from_array([4]))
    	print to_array(first)
        self.assertEqual(to_array(first), [1,2,3,4], 'one long')


if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
