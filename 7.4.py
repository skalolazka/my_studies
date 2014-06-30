#!/usr/bin/env python

from mynode import *
import unittest

def ll_are_joined(ll1, ll2):
    ptr1, ptr2 = ll1, ll2
    if ptr1 is None or ptr2 is None:
        return None
    lens = [0, 0] # count lengths
    i = 0
    for ptr in (ptr1, ptr2):
        while ptr is not None:
            lens[i] += 1
            ptr = ptr.next_node
        i += 1
    if lens[0] > lens[1]:
        ll1, ll2 = ll2, ll1
        lens[0], lens[1] = lens[1], lens[0]
    # now ll1 is the shorter list
    while lens[1] > lens[0]:
        ll2 = ll2.next_node
        lens[1] -= 1
    while ll1 is not None:
        if ll1 is ll2:
            return ll1
        ll1, ll2 = ll1.next_node, ll2.next_node
    return None


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
