#!/usr/bin/env python

from linkedlist import LinkedList

def merge_ll(l1, l2):
    ptr1, ptr2 = l1.first, l2.first
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
#        self.assertTrue(True)
#        first = merge_ll(LinkedList([2,5,6,7,8]), LinkedList([3,4,9,10,11,12,13]))
        first = merge_ll(LinkedList([2]), LinkedList([3]))
        if first == LinkedList([2,3]):
            print 'ok'
        self.assertEqual(first, LinkedList([2,3]).first)

#while 1:
#    print first.value
#    if first.next_node is None:
#        break
#    first = first.next_node


if __name__ == '__main__':
    unittest.main()
