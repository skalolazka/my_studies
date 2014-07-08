#!/usr/bin/env python

# task: lowest common ancestor of two nodes

from mybintree_8_9 import *

class MyBinTreeWithParent(MyBinTree):
    def __init__(self, value=None):
        MyBinTree.__init__(self, value)
        self.parent = None

    def put_left(self, value): # oh well, copypaste...
        MyBinTree.put_left(self, value)
#        if isinstance(value, MyBinTreeWithParent):
#            self.left = value
#        else:
#            self.left = MyBinTreeWithParent(value)
        self.left.parent = self

    def put_right(self, value):
        if isinstance(value, MyBinTreeWithParent):
            self.right = value
        else:
            self.right = MyBinTreeWithParent(value)
        self.right.parent = self


def lca(t1, t2):
    if t1 is None or t2 is None:
        return None # watch it!
    len1, len2 = way_len(t1), way_len(t2)
    if len1 > len2:
        t1, t2 = t2, t1
        len1, len2 = len2, len1
    # now t1 is the node with the sorter way to the top
    while len2 > len1:
        t2 = t2.parent
        len2 -= 1
    while t1 is not t2:
        t1, t2 = t1.parent, t2.parent
    return t1


def way_len(t):
    if t is None:
        return None
    result = 0
    p = t.parent
    while p is not None:
        p = p.parent
        result += 1
    return result

import unittest

class TestMyBinTree(unittest.TestCase):
    def test_init(self):
        t = MyBinTreeWithParent()
        self.assertIsInstance(t, MyBinTree, 'parent class')
        self.assertIsInstance(t, MyBinTreeWithParent, 'this class')
        self.assertEqual(t.value, None, 'no value')
        self.assertEqual(t.left, None, 'no left')
        self.assertEqual(t.right, None, 'no right')
        self.assertEqual(t.parent, None, 'no parent')
        t = MyBinTreeWithParent(3)
        self.assertIsInstance(t, MyBinTree, 'parent class 1')
        self.assertIsInstance(t, MyBinTreeWithParent, 'this class 1')
        self.assertEqual(t.value, 3, 'value ok')
        self.assertEqual(t.left, None, 'no left still')
        self.assertEqual(t.right, None, 'no right still')
        self.assertEqual(t.parent, None, 'no parent still')

    def test_put(self):
        t = MyBinTreeWithParent(2)
        t.put_left(3)
        self.assertIsInstance(t.left, MyBinTree, 'parent class')
        self.assertIsInstance(t.left, MyBinTreeWithParent, 'this class')
        self.assertEqual(t.left.value, 3, 'left value')
        self.assertEqual(t.left.left, None, 'no left.left')
        self.assertEqual(t.left.right, None, 'no left.right')
        self.assertEqual(t.left.parent, t, 'parent - top')
        t.put_right(MyBinTreeWithParent(4))
        self.assertIsInstance(t.right, MyBinTree, 'parent class for right')
        self.assertIsInstance(t.right, MyBinTreeWithParent, 'this class for right')
        self.assertEqual(t.right.parent, t, 'right parent - top')
        t.left.put_left(5)
        self.assertEqual(t.left.left.parent, t.left, 'parent - left')

    def test_way_len(self):
        self.assertEqual(way_len(None), None, 'None - path None')
        t = MyBinTreeWithParent(2)
        self.assertEqual(way_len(t), 0, 'root path 0')
        t.put_left(3)
        self.assertEqual(way_len(t.left), 1, 'child path 1')
        t.put_right(MyBinTreeWithParent(4))
        self.assertEqual(way_len(t.right), 1, 'child path 1 too')
        t.left.put_left(5)
        t.left.left.put_right(6)
        self.assertEqual(way_len(t.left.left.right), 3, 'node path 3')
        t.left.left.right.put_right(7)
        self.assertEqual(way_len(t.left.left.right.right), 4, 'node path 4')

    def test_lca(self):
        self.assertEqual(lca(None, None), None, 'None for None, None')
        t1 = MyBinTreeWithParent(2)
        self.assertEqual(lca(None, t1), None, 'None for None, t1')
        self.assertEqual(lca(t1, None), None, 'None for t1, None')
        t2 = MyBinTreeWithParent(3)
        self.assertEqual(lca(t1, t2), None, 'None for separate trees')
        t1.put_left(21)
        self.assertEqual(lca(t1, t1.left), t1, 'root for root and child')
        t1.put_right(22)
        self.assertEqual(lca(t1.right, t1.left), t1, 'root for children')
        t1.left.put_left(23)
        t1.left.put_right(24)
        self.assertEqual(lca(t1.left.right, t1.left.left), t1.left, 'child for children')
        t1.left.left.put_left(25)
        t1.left.left.left.put_right(26)
        t1.left.left.left.right.put_right(27)
        self.assertEqual(lca(t1.left.right, t1.left.left.left.right), t1.left, 'child for faraway children')
        self.assertEqual(lca(t1.right, t1.left.left.left.right), t1, 'root for faraway children')
        t1.right.put_left(28)
        self.assertEqual(lca(t1.right.left, t1.left.left.left.right), t1, 'root for faraway children again')
        t2.put_left(44)
        self.assertEqual(lca(t2.left, t1.left.left.left.right), None, 'None for children of separate trees')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMyBinTree)
    unittest.TextTestRunner(verbosity=2).run(suite)
