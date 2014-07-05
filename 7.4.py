#!/usr/bin/env python

from mynode import *
import unittest

def ll_are_joined(ll1, ll2):
    if ll1 is None or ll2 is None:
        return None
    len1 = length(ll1) # count lengths
    len2 = length(ll2)
    if len1 > len2:
        ll1, ll2 = ll2, ll1
        len1, len2 = len2, len1
    # now ll1 is the shorter list
    while len2 > len1:
        ll2 = ll2.next_node
        len2 -= 1
    while ll1 is not ll2:
        ll1, ll2 = ll1.next_node, ll2.next_node
    return ll1

def length(ll):
    length = 0
    while ll is not None:
        length += 1
        ll = ll.next_node
    return length


class MyTest(unittest.TestCase):

    def test_small(self):
        first = ll_are_joined(from_array([]), from_array([]))
        self.assertEqual(first, None, 'empty')

        first = ll_are_joined(from_array([1]), from_array([]))
        self.assertEqual(first, None, 'still empty')

        first = ll_are_joined(from_array([]), from_array([1]))
        self.assertEqual(first, None, 'still empty again')

    def test_not_joined(self):
        first = ll_are_joined(from_array([2]), from_array([3]))
        self.assertEqual(first, None, 'one and one, not joined')

        first = ll_are_joined(from_array([2,3,4,5]), from_array([2,3,4,5]))
        self.assertEqual(first, None, 'not joined still')

    def test_joined(self):
        ll1, ll2 = from_array([1,3]), from_array([2,3])
        ll1.next_node = ll2.next_node
        first = ll_are_joined(ll1, ll2)
        self.assertEqual(first.value, 3, 'same len, last elem')

        ll1, ll2 = from_array([1,3,4]), from_array([2,3,5,6,7])
        ll1.next_node = ll2.next_node
        first = ll_are_joined(ll1, ll2)
        self.assertEqual(first.value, 3, 'same len, not last elem')

        ll1, ll2 = from_array([1,2,3,4]), from_array([4,5,6])
        ll1.next_node.next_node = ll2
        first = ll_are_joined(ll1, ll2)
        self.assertEqual(first.value, 4, 'joined at the start of second list')

        ll1, ll2 = from_array([1,2]), from_array([4,5,6])
        ll1.next_node.next_node = ll2.next_node
        first = ll_are_joined(ll1, ll2)
        self.assertEqual(first.value, 5, 'joined at the end of first list')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
