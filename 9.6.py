#!/usr/bin/env python

# task: k-th node in inorder, each node has number of nodes in subtree

from mybintree_8_9 import *

class MyBinTreeWithSubtreeSize(MyBinTree):
    def __init__(self, value=None):
        MyBinTree.__init__(self, value)
        self.subtree_size = 1
    def put_left(self, value):
        MyBinTree.put_left(self, value)
        self.left.subtree_size = 1
        # after this one needs to call subtree_size_update()
        # for the full tree himself!!! or is there a better way??

def subtree_size_update(t):
    if t is None:
        return 0
    t.subtree_size = subtree_size_update(t.left) + subtree_size_update(t.right) + 1
    return t.subtree_size

def k_th_node (t, k):
    if t is None or k == 0:
        return None # let's start counting from 1
    while k > 0 and t is not None:
        if t.left is None:
            if k == 1:
                return t
            else:
                k = k - 1
                t = t.right
        elif t.left.subtree_size == k - 1:
            return t
        elif t.left.subtree_size < k - 1: # go right
            k = k - t.left.subtree_size - 1
            t = t.right
        else: # t.left.subtree_size > k - 1 - go left
            t = t.left
    return t


import unittest

class TestKthNode(unittest.TestCase):
    def setUp(self):
        self.root = MyBinTreeWithSubtreeSize(1)
        self.with_left = MyBinTreeWithSubtreeSize(1)
        self.with_left.put_left(2)
        subtree_size_update(self.with_left)
        self.with_two = MyBinTreeWithSubtreeSize(1)
        self.with_two.put_left(2)
        self.with_two.put_right(3)
        subtree_size_update(self.with_two)
        #       5
        #      / \
        #     3   6
        #    / \   \
        #   2   4   8
        #  /       /
        # 1       7
        self.big = MyBinTreeWithSubtreeSize(5)
        self.big.put_left(3)
        self.big.left.put_left(2)
        self.big.left.left.put_left(1)
        self.big.left.put_right(4)
        self.big.put_right(6)
        self.big.right.put_right(8)
        self.big.right.right.put_left(7)
        subtree_size_update(self.big)

    def test_subtree_size_update(self):
        self.assertEqual(subtree_size_update(self.root), 1, '1 for root')
        self.assertEqual(self.root.subtree_size, 1, 'really in the tree for root')
        self.assertEqual(self.big.subtree_size, 8, 'big - root')
        self.assertEqual(self.big.left.subtree_size, 4, 'big - left')
        self.assertEqual(self.big.left.left.subtree_size, 2, 'big - left.left')
        self.assertEqual(self.big.left.left.left.subtree_size, 1, 'big - left.left.left')
        self.assertEqual(self.big.left.right.subtree_size, 1, 'big - left.right')
        self.assertEqual(self.big.right.subtree_size, 3, 'big - right')
        self.assertEqual(self.big.right.right.subtree_size, 2, 'big - right.right')
        self.assertEqual(self.big.right.right.left.subtree_size, 1, 'big - right.right.left')

    def test_empty(self):
        self.assertEqual(k_th_node(None, 0), None, 'None, 0')
        self.assertEqual(k_th_node(self.root, 0), None, 'tree, 0')

    def test_one(self):
        self.assertEqual(k_th_node(self.root, 1), self.root, 'k=1, tree = just root')
        self.assertEqual(k_th_node(self.root, 2), None, 'k=2, tree = just root')

    def test_one_child(self):
        self.assertEqual(k_th_node(self.with_left, 1), self.with_left.left, 'k=1, tree = left child')
        self.assertEqual(k_th_node(self.with_left, 2), self.with_left, 'k=2, tree = left child')
        self.assertEqual(k_th_node(self.with_left, 3), None, 'k=3, tree = left child')

    def test_two_children(self):
        self.assertEqual(k_th_node(self.with_two, 1), self.with_two.left, 'k=1, tree = two children')
        self.assertEqual(k_th_node(self.with_two, 2), self.with_two, 'k=2, tree = two children')
        self.assertEqual(k_th_node(self.with_two, 3), self.with_two.right, 'k=3, tree = two children')

    def test_many(self):
        self.assertEqual(k_th_node(self.big, 1), self.big.left.left.left, '1')
        self.assertEqual(k_th_node(self.big, 2), self.big.left.left, '2')
        self.assertEqual(k_th_node(self.big, 3), self.big.left, '3')
        self.assertEqual(k_th_node(self.big, 4), self.big.left.right, '4')
        self.assertEqual(k_th_node(self.big, 5), self.big, '5')
        self.assertEqual(k_th_node(self.big, 6), self.big.right, '6')
        self.assertEqual(k_th_node(self.big, 7), self.big.right.right.left, '7')
        self.assertEqual(k_th_node(self.big, 8), self.big.right.right, '8')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestKthNode)
    unittest.TextTestRunner(verbosity=2).run(suite)
