#!/usr/bin/env python

# task: k-th node in inorder, each node has number of nodes in subtree

from mybintree_8_9 import *

def k_th_node (t, k):
    if t is None or k is None or k == 0:
        return None # let's start counting from 1
    while k > 0 and t is not None:
        if t.left is None:
            if k == 1:
                return t
            else:
                k = k - 1
                t = t.right
        elif t.left.subtree == k - 1:
            return t
        elif t.left.subtree < k - 1: # go right
            k = k - t.left.subtree - 1
            t = t.right
        else: # t.left.subtree > k - 1 - go left
            t = t.left
    return t


import unittest

class TestKthNode(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(k_th_node(None, None), None, 'None, None')
        self.assertEqual(k_th_node(None, 0), None, 'None, 0')
        t = MyBinTree(1)
        self.assertEqual(k_th_node(t, 0), None, 'tree, 0')

    def test_one(self):
        t = MyBinTree(1)
        t.subtree = 1
        self.assertEqual(k_th_node(t, 1), t, 'k=1, tree = just root')
        self.assertEqual(k_th_node(t, 2), None, 'k=2, tree = just root')

    def test_one_child(self):
        t = MyBinTree(1)
        t.put_left(2)
        t.subtree = 2
        t.left.subtree = 1
        self.assertEqual(k_th_node(t, 1), t.left, 'k=1, tree = left child')
        self.assertEqual(k_th_node(t, 2), t, 'k=2, tree = left child')
        self.assertEqual(k_th_node(t, 3), None, 'k=3, tree = left child')

    def test_two_children(self):
        t = MyBinTree(1)
        t.put_left(2)
        t.put_right(3)
        t.subtree = 3
        t.left.subtree = 1
        t.right.subtree = 1
        self.assertEqual(k_th_node(t, 1), t.left, 'k=1, tree = two children')
        self.assertEqual(k_th_node(t, 2), t, 'k=2, tree = two children')
        self.assertEqual(k_th_node(t, 3), t.right, 'k=3, tree = two children')

    def test_many(self):
        #       5
        #      / \
        #     3   6
        #    / \   \
        #   2   4   8
        #  /       /
        # 1       7
        # I'm REEEALLY lazy for writing a function that counts the "subtree" number. but I'm sure I'm able to.
        t = MyBinTree(5)
        t.put_left(3)
        t.left.put_left(2)
        t.left.left.put_left(1)
        t.left.put_right(4)
        t.put_right(6)
        t.right.put_right(8)
        t.right.right.put_left(7)
        t.subtree = 8
        t.left.subtree = 4
        t.left.left.subtree = 2
        t.left.left.left.subtree = 1
        t.left.right.subtree = 1
        t.right.subtree = 3
        t.right.right.subtree = 2
        t.right.right.left.subtree = 1
        self.assertEqual(k_th_node(t, 1), t.left.left.left, '1')
        self.assertEqual(k_th_node(t, 2), t.left.left, '2')
        self.assertEqual(k_th_node(t, 3), t.left, '3')
        self.assertEqual(k_th_node(t, 4), t.left.right, '4')
        self.assertEqual(k_th_node(t, 5), t, '5')
        self.assertEqual(k_th_node(t, 6), t.right, '6')
        self.assertEqual(k_th_node(t, 7), t.right.right.left, '7')
        self.assertEqual(k_th_node(t, 8), t.right.right, '8')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestKthNode)
    unittest.TextTestRunner(verbosity=2).run(suite)
