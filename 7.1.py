#!/usr/bin/env python

from mylinkedlist import MyLinkedList

def merge_ll(l1, l2):
    ptr1, ptr2 = l1.first, l2.first
    if ptr1.value is None:
        return ptr2
    if ptr2.value is None:
        return ptr1
    prev1, prev2 = l1.first, l2.first
    first = None
    while 1:
        old_next1, old_next2 = ptr1.next_node, ptr2.next_node
        if ptr1.value < ptr2.value:
            if old_next1 is None or old_next1.value > ptr2.value:
                if first is None:
                    first = ptr1
                ptr1.next_node = ptr2
                if old_next1 is None:
                    break
                ptr1 = old_next1
            else:
                ptr1 = old_next1
        else:
            if old_next2 is None or old_next2.value > ptr1.value:
                if first is None:
                    first = ptr2
                ptr2.next_node = ptr1
                if old_next2 is None:
                    break
                ptr2 = old_next2
            else:
                ptr2 = old_next2
    return first



import unittest

class SimplisticTest(unittest.TestCase):

    def test(self):
        first = merge_ll(MyLinkedList(), MyLinkedList())
        self.assertEqual(first, MyLinkedList().first, 'empty')
        first = merge_ll(MyLinkedList([2]), MyLinkedList())
        self.assertEqual(first, MyLinkedList([2]).first, 'one empty')
        first = merge_ll(MyLinkedList(), MyLinkedList([3]))
        self.assertEqual(first, MyLinkedList([3]).first)
        first = merge_ll(MyLinkedList([2]), MyLinkedList([3]))
        self.assertEqual(first, MyLinkedList([2,3]).first)
        first = merge_ll(MyLinkedList([3]), MyLinkedList([2]))
        self.assertEqual(first, MyLinkedList([2,3]).first)
        first = merge_ll(MyLinkedList([2,5]), MyLinkedList([3]))
        self.assertEqual(first, MyLinkedList([2,3,5]).first)
        first = merge_ll(MyLinkedList([2,5,5]), MyLinkedList([3,4,4]))
        self.assertEqual(first, MyLinkedList([2,3,4,4,5,5]).first)
        first = merge_ll(MyLinkedList([2,5,6,7,8]), MyLinkedList([3,4,9,10,11,12,13]))
        self.assertEqual(first, MyLinkedList([2,3,4,5,6,7,8,9,10,11,12,13]).first)
        first = merge_ll(MyLinkedList([2,4,6,8]), MyLinkedList([3,6,7,9]))
        self.assertEqual(first, MyLinkedList([2,3,4,5,6,7,8,9]).first)

if __name__ == '__main__':
    unittest.main()
