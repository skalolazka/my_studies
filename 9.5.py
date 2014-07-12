#!/usr/bin/env python

# task: in-o w.parent pointers, O(1) space

#from mybintree_8_9 import *
from mybintree_w_parent_9_12 import MyBinTreeWithParent

def inorder_w_parent(t):
    result = []
    child = None
    while t is not None: # will happen only when we come to root.parent, other cases are checked
        go_right = 0
        if child is not None and t.left == child: # came here from left child
            result.append(t.value)
            go_right = 1
        elif child is not None and t.right == child: # came here from right child
            child = t
            t = t.parent
        else: # first time is this node
            if t.left is None: # can't go left
                result.append(t.value)
                go_right = 1
            else: # go left first
                child = None
                t = t.left
        if go_right: # just took this repeating block of code out
            if t.right is None: # can't go right - go up
                child = t
                t = t.parent
            else:
                child = None
                t = t.right

    return result

import unittest

class TestInOrderWParent(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(inorder_w_parent(None), [], 'None')

    def test_many(self):
        t = MyBinTreeWithParent(1)
        self.assertEqual(inorder_w_parent(t), [1], 'just root')
        t.put_left(2)
        self.assertEqual(inorder_w_parent(t), [2, 1], 'root with left child')
        t.put_right(3)
        self.assertEqual(inorder_w_parent(t), [2, 1, 3], 'root with two children')
        #      1
        #     / \
        #    2   3
        #   / \   \
        #  4   5   6
        #   \
        #    7
        t.left.put_left(4)
        t.left.put_right(5)
        self.assertEqual(inorder_w_parent(t), [4, 2, 5, 1, 3], 'big tree')
        t.right.put_right(6)
        self.assertEqual(inorder_w_parent(t), [4, 2, 5, 1, 3, 6], 'bigger tree')
        t.left.left.put_right(7)
        self.assertEqual(inorder_w_parent(t), [4, 7, 2, 5, 1, 3, 6], 'even bigger tree')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestInOrderWParent)
    unittest.TextTestRunner(verbosity=2).run(suite)
