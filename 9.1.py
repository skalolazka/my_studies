#!/usr/bin/env python

from mybintree_8_9 import *

def is_balanced(t):
    if t is None:
        return True # empty tree is balanced, right?
    if not isinstance(t, MyBinTree):
        raise TypeError
    return height(t)[0]

def height(t):
    if t is None:
        return (True, 0)
    result1, height1 = height(t.left)
    result2, height2 = height(t.right)
    h = max(height1, height2) + 1
    if result1 is False or result2 is False or abs(height1 - height2) > 1:
        return (False, h)
    else:
        return (True, h)


import unittest

class MyIsBalancedTest(unittest.TestCase):
    def test_wrong_type(self):
        self.assertRaises(TypeError, is_balanced, 1)

    def test_empty(self):
        self.assertEqual(is_balanced(MyBinTree()), True, 'empty tree is balanced, right?')

    def test_one(self):
        self.assertEqual(is_balanced(MyBinTree(2)), True, 'one node is balanced')

    def test_many(self):
        t = MyBinTree(1)
        t.put_left(2)
        self.assertEqual(is_balanced(t), True, 'one left child')
        t.put_right(3)
        self.assertEqual(is_balanced(t), True, 'two children')
        t.left.put_left(4)
        self.assertEqual(is_balanced(t), True, 'two children, one has one child')
        t.left.left.put_left(5)
        self.assertEqual(is_balanced(t), False, 'not balanced now')
        t.left.put_right(6)
        self.assertEqual(is_balanced(t), False, 'still not balanced')
        t.right.put_left(7)
        t.right.put_right(8)
        self.assertEqual(is_balanced(t), True, 'balanced now')
        t = MyBinTree(1)
        t.put_left(2)
        t.put_right(3)
        t.left.put_left(4)
        t.right.put_right(5)
        self.assertEqual(is_balanced(t), True, 'weird, but balanced')
        t.right.right.put_right(6)
        self.assertEqual(is_balanced(t), False, 'not balanced now!')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyIsBalancedTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
