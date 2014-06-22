#!/usr/bin/env python

import unittest
from mybintree import *

class TestMyBinTree(unittest.TestCase):
    def test_init(self):
        t = MyBinTree()
        self.assertIsInstance(t, MyBinTree, 'object created')
        self.assertEqual(t.value, None, 'no value')
        self.assertEqual(t.left, None, 'no left')
        self.assertEqual(t.right, None, 'no right')
        t = MyBinTree(3)
        self.assertIsInstance(t, MyBinTree, 'object created')
        self.assertEqual(t.value, 3, 'value ok')
        self.assertEqual(t.left, None, 'no left still')
        self.assertEqual(t.right, None, 'no right still')

    def test_put(self):
        t = MyBinTree(2)
        t.put_left(3)
        self.assertEqual(t.left.value, 3, 'left value')
        self.assertEqual(t.left.left, None, 'no left.left')
        self.assertEqual(t.left.right, None, 'no left.right')
        self.assertEqual(t.right, None, 'no right')
        t.put_right(MyBinTree(5))
        self.assertIsInstance(t.right, MyBinTree, 'object created')
        print t.right.value
        self.assertIsInstance(t.right.value, int, 'normal int value')
        self.assertEqual(t.right.value, 5, 'right value')
        self.assertEqual(t.right.left, None, 'no right.left')
        self.assertEqual(t.right.right, None, 'no right.right')

    def test_print_by_levels(self):
        t = MyBinTree()
        self.assertEqual(t.array_by_levels(), [], 'none')
        t1 = MyBinTree(4)
        self.assertEqual(t1.array_by_levels(), [4], 'one')
        #      1
        #     / \
        #    2   3
        #   /\    \
        #  4  5    6
        # /    \    \
        #7      8    9
        t1.put_left(7)
        self.assertEqual(t1.array_by_levels(), [4,7], 'two')
        t2 = MyBinTree(5)
        t2.put_right(8)
        self.assertEqual(t2.array_by_levels(), [5,8], 'two (right)')
        t3 = MyBinTree(2)
        t3.put_left(t1)
        t3.put_right(t2)
        tm = MyBinTree(1)
        tm.put_left(t3)
        self.assertEqual(tm.array_by_levels(), [1,2,4,5,7,8], 'one left subtree')
        t4 = MyBinTree(6)
        t4.put_right(9)
        t5 = MyBinTree(3)
        t5.put_right(t4)
        tm.put_right(t5)
        self.assertEqual(tm.array_by_levels(), [1,2,3,4,5,6,7,8,9], 'printed long')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMyBinTree)
    unittest.TextTestRunner(verbosity=2).run(suite)
