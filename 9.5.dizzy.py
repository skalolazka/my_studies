#!/usr/bin/env python

# task: in-o w.parent pointers, O(1) space
# I can't say this one looks better! But I couldn't make the part with "go right" better - 
# either it's copypaste in two if's, or a function, both look ugly.

from mybintree_w_parent_9_12 import MyBinTreeWithParent

def next_inorder_node(node):
    if node.left is not None:
        while node.left is not None:
            node = node.left
        return node
    else:
        return node # ?!
 
def go_right(t):
    prev = None
    if t.right is not None:
        t = next_inorder_node(t.right)
    else:
        prev = t
        t = t.parent
    return (t, prev)

def inorder_w_parent(t):
    result = []
    prev = None
    while t is not None: # will happen only when we come to root.parent, other cases are checked
        if prev is None:
            t = next_inorder_node(t)
            if t == t: # no left node
                result.append(t.value)
                (t, prev) = go_right(t)
        elif prev == t.left: # came from left child
            prev = None
            result.append(t.value)
            (t, prev) = go_right(t)
        else: # came from right child
            prev = t
            t = t.parent
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
