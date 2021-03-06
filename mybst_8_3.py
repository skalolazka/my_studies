#!/usr/bin/env python

from mystack_8_1 import *
from mybintree_8_9 import *

class MyBST(MyBinTree):
    def __init__(self, value=None):
        MyBinTree.__init__(self, value)

    def put_value(self, value):
        if self.value is None:
            self.value = value
            return self
        cur = self
        prev = cur
        which = None
        while cur is not None:
            prev = cur
            if value < cur.value:
                cur = cur.left
                which = 'left'
            else:
                cur = cur.right
                which = 'right'
        if which is not None:
            if which == 'left':
                prev.left = MyBST(value)
            else:
                prev.right = MyBST(value)

    def put_value_var2(self, value):
        cur = self
        while cur is not None:
            if value < cur.value:
                if cur.left is None:
                    cur.left = MyBST(value)
                    break
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = MyBST(value)
                    break
                cur = cur.right


def from_array(values):
    b = MyBST()
    for v in values:
        b.put_value(v)
    return b

def to_array(b):
    if b is None:
        return []
    cur = b
    arr = []
    s = MyStack()
    while cur is not None or not s.is_empty():
        if cur is None:
            cur = s.pop()
            arr.append(cur.value)
            cur = cur.right
        else:
            s.push(cur)
            cur = cur.left
    return arr


import unittest

class Test_MyBST(unittest.TestCase):
    def test_init(self):
        b = MyBST()
        self.assertEqual(b.value, None, 'no value')
        self.assertEqual(b.left, None, 'no left')
        self.assertEqual(b.right, None, 'no right')
        b = MyBST(2)
        self.assertEqual(b.value, 2, 'value')
        self.assertEqual(b.left, None, 'no left still')
        self.assertEqual(b.right, None, 'no right still')

    def test_put(self):
        b = MyBST()
        b.put_value(1)
        self.assertEqual(b.value, 1, 'value')
        self.assertEqual(b.left, None, 'no left')
        self.assertEqual(b.right, None, 'no right')
        b.put_value(2)
        self.assertEqual(b.value, 1, 'same value')
        self.assertEqual(b.left, None, 'no left still')
        self.assertIsInstance(b.right, MyBST, 'right subtree')
        self.assertEqual(b.right.value, 2, 'put into right')
        self.assertEqual(b.right.left, None, 'right - no left')
        self.assertEqual(b.right.right, None, 'right - no right')
        b.put_value(0)
        self.assertEqual(b.value, 1, 'same value')
        self.assertIsInstance(b.left, MyBST, 'left subtree')
        self.assertEqual(b.right.value, 2, 'right still there')
        self.assertEqual(b.left.value, 0, 'put into left')
        self.assertEqual(b.right.left, None, 'right - no left still')
        self.assertEqual(b.right.right, None, 'right - no right still')
        self.assertEqual(b.left.left, None, 'left - no left still')
        self.assertEqual(b.left.right, None, 'left - no right still')
        b.put_value(3)
        self.assertEqual(b.value, 1, 'same value')
        self.assertEqual(b.right.value, 2, 'right still there')
        self.assertEqual(b.left.value, 0, 'left still there')
        self.assertEqual(b.right.right.value, 3, 'put into very right')

    def test_to_array(self):
        self.assertEqual(to_array(None), [], 'empty')
        b = MyBST(1)
        self.assertEqual(to_array(b), [1], 'one')
        b.put_value(0)
        self.assertEqual(to_array(b), [0, 1], 'two')
        b.put_value(2)
        self.assertEqual(to_array(b), [0, 1, 2], 'three')
        b.put_value(5)
        self.assertEqual(to_array(b), [0, 1, 2, 5], 'four')
        b.put_value(3)
        self.assertEqual(to_array(b), [0, 1, 2, 3, 5], 'five')
        b = from_array([5,1,2,3,10])
        self.assertEqual(to_array(b), [1, 2, 3, 5, 10], 'six')

    def test_from_array(self):
        b = from_array([])
        self.assertIsInstance(b, MyBST, 'instance')
        self.assertEqual(b.value, None, 'no val')
        self.assertEqual(b.left, None, 'no left')
        self.assertEqual(b.right, None, 'no right')
        b = from_array([1])
        self.assertIsInstance(b, MyBST, 'instance now too')
        self.assertEqual(b.value, 1, 'val')
        self.assertEqual(b.left, None, 'no left still')
        self.assertEqual(b.right, None, 'no right still')
        b = from_array([5,1,2,3,10])
        self.assertEqual(b.value, 5, 'head val')
        self.assertEqual(b.left.value, 1, 'put 1')
        self.assertEqual(b.left.right.value, 2, 'put 2')
        self.assertEqual(b.left.right.right.value, 3, 'put 3')
        self.assertEqual(b.right.value, 10, 'put 10')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_MyBST)
    unittest.TextTestRunner(verbosity=2).run(suite)
