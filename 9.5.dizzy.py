#!/usr/bin/env python

# task: in-o w.parent pointers, O(1) space

from mybintree_w_parent_9_12 import MyBinTreeWithParent

def leftmost_child(node):
    while node.left is not None:
        node = node.left
    return node

def next_inorder_node(node):
    if node.right is not None:
        return leftmost_child(node.right)
    else:
        prev = node
        while node is not None and prev != node.left:
            prev = node
            node = node.parent
        return node

def inorder_w_parent(t):
    if t is None:
        return []
    result = []
    prev = None
    t = leftmost_child(t)
    while t is not None: # will happen only when we come to root.parent, other cases are checked
        result.append(t.value)
        t = next_inorder_node(t)
    return result

import unittest

class TestInOrderWParent(unittest.TestCase):
    def setUp(self):
        self.root = MyBinTreeWithParent(1)
        self.left_child = MyBinTreeWithParent(1)
        self.left_child.put_left(2)
        self.children = MyBinTreeWithParent(1)
        self.children.put_left(2)
        self.children.put_right(3)
        self.tree = MyBinTreeWithParent(1)
        self.tree.put_left(2)
        self.tree.put_right(3)
        self.tree.left.put_left(4)
        self.tree.left.put_right(5)
        self.big_tree = MyBinTreeWithParent(1)
        self.big_tree.put_left(2)
        self.big_tree.put_right(3)
        self.big_tree.left.put_left(4)
        self.big_tree.left.put_right(5)
        self.big_tree.right.put_right(6)
        self.big_tree.left.left.put_right(7)
        #      1
        #     / \
        #    2   3
        #   / \   \
        #  4   5   6
        #   \
        #    7

    def test_leftmost_child(self):
        aa = leftmost_child(self.big_tree)
        self.assertEqual(leftmost_child(self.big_tree), self.big_tree.left.left, 'leftmost child of root')
        self.assertEqual(leftmost_child(self.big_tree.left), self.big_tree.left.left, 'leftmost child of root.left')
        self.assertEqual(leftmost_child(self.big_tree.right), self.big_tree.right, 'leftmost child of root.right')

    def test_next_inorder_node(self):
        self.assertEqual(next_inorder_node(self.root), None, 'root')
        self.assertEqual(next_inorder_node(self.big_tree), self.big_tree.right, 'root of big tree')
        self.assertEqual(next_inorder_node(self.big_tree.left.left), self.big_tree.left.left.right, 'left-left')
        self.assertEqual(next_inorder_node(self.big_tree.left.left.right), self.big_tree.left, 'left-left-right')
        self.assertEqual(next_inorder_node(self.big_tree.left.right), self.big_tree, 'left-right')
        self.assertEqual(next_inorder_node(self.big_tree.right.right), None, 'right-right')

    def test_empty(self):
        self.assertEqual(inorder_w_parent(None), [], 'None')

    #@unittest.skip('later')
    def test_many(self):
        self.assertEqual(inorder_w_parent(self.root), [1], 'just root')
        self.assertEqual(inorder_w_parent(self.left_child), [2, 1], 'root with left child')
        self.assertEqual(inorder_w_parent(self.children), [2, 1, 3], 'root with two children')
        self.assertEqual(inorder_w_parent(self.tree), [4, 2, 5, 1, 3], 'big tree')
        self.assertEqual(inorder_w_parent(self.big_tree), [4, 7, 2, 5, 1, 3, 6], 'even bigger tree')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestInOrderWParent)
    unittest.TextTestRunner(verbosity=2).run(suite)
