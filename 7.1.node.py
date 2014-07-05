#!/usr/bin/env python

# task: merge two linked lists in ascending order of the values

from mynode import *
import unittest

def merge_ll(ptr1, ptr2):
    if ptr1 is None or ptr2 is None:
        return ptr2 or ptr1
    ptrs = [ptr1, ptr2]
    head = MyNode()
    first = head
    while ptrs[0] is not None and ptrs[1] is not None:
        which = 0 if ptrs[0].value < ptrs[1].value else 1
        old_next = ptrs[which].next_node
        head.next_node = ptrs[which]
        ptrs[which] = old_next
        head = head.next_node
    if ptrs[0] is not None or ptrs[1] is not None:
        head.next_node = ptrs[0] or ptrs[1]
    return first.next_node

def recursive_merge_ll(ptr1, ptr2):
    if ptr1 is None or ptr2 is None:
        return ptr2 or ptr1
    if ptr1.value > ptr2.value:
        ptr1, ptr2 = ptr2, ptr1
    ptr1.next_node = recursive_merge_ll(ptr1.next_node, ptr2)
    return ptr1


class MyBaseTest(unittest.TestCase):
    def test_empty(self):
        func = self.get_func()

        first = func(from_array([]), from_array([]))
        self.assertEqual(first, None, 'empty')

        first = func(from_array([None]), from_array([None]))
        self.assertIsInstance(first, MyNode, 'class')
        self.assertEqual(first.value, None, 'no value')
        self.assertEqual(first.value, None, 'no next')

        first = func(from_array([0]), from_array([]))
        self.assertEqual(to_array(first), [0], 'one empty, val 0')

        first = func(from_array([2]), from_array([]))
        self.assertEqual(to_array(first), [2], 'one empty, val 2')

        first = func(None, from_array([3]))
        self.assertEqual(to_array(first), [3], 'first empty')

        first = func(None, from_array([0]))
        self.assertEqual(to_array(first), [0], 'first empty, val = 0')

    def test_one(self):
        func = self.get_func()
        first = func(from_array([2]), from_array([3]))
        self.assertEqual(to_array(first), [2,3], 'one elem in each')

        first = func(from_array([3]), from_array([2]))
        self.assertEqual(to_array(first), [2,3], 'first one bigger')

    def test_many(self):
        func = self.get_func()
        first = func(from_array([2,5]), from_array([3]))
        self.assertEqual(to_array(first), [2,3,5], 'two and one in the middle')

        first = func(from_array([2,5,5]), from_array([3,4,4]))
        self.assertEqual(to_array(first), [2,3,4,4,5,5], 'same values')

        first = func(from_array([2,5,6,7,8]), from_array([3,4,9,10,11,12,13]))
        self.assertEqual(to_array(first), [2,3,4,5,6,7,8,9,10,11,12,13], 'long=)')

        first = func(from_array([2,4,6,8]), from_array([3,5,7,9]))
        self.assertEqual(to_array(first), [2,3,4,5,6,7,8,9], 'zig-zag=)')

    def test_one_long(self):
        func = self.get_func()
        first = func(from_array([1,2,3]), from_array([4]))
        self.assertEqual(to_array(first), [1,2,3,4], 'one long')


class MergeLLTest(MyBaseTest):
    def get_func(self):
        return merge_ll


class RecursiveMergeLLTest(MyBaseTest):
    def get_func(self):
        return recursive_merge_ll


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MergeLLTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
    suite = unittest.TestLoader().loadTestsFromTestCase(RecursiveMergeLLTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
