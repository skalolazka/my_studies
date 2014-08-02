#!/usr/bin/env python

from mybst_8_3 import *

def from_preorder(preorder, start=None, end=None):
    if start is None:
        start, end = 0, len(preorder)
    if start == end:
        return None
    root = preorder[start]
    result = MyBST(root)
    left_part = start + 1
    while left_part < end and preorder[left_part] <= root:
        left_part += 1
    result.put_left(from_preorder(preorder, start + 1, left_part))
    result.put_right(from_preorder(preorder, left_part, end))
    return result


import unittest

class Test_MyBST(unittest.TestCase):
    def test_very_short(self):
        b = from_preorder([])
        self.assertEqual(b, None, 'nothing')
        b = from_preorder([1])
        self.assertEqual(b.value, 1, 'value')
        self.assertEqual(b.left, None, 'no left')
        self.assertEqual(b.right, None, 'no right')

    def test_short(self):
        b = from_preorder([2,1])
        self.assertEqual(b.value, 2, 'value')
        self.assertEqual(b.left.value, 1, 'left')
        self.assertEqual(b.right, None, 'no right')
        b = from_preorder([2,3])
        self.assertEqual(b.value, 2, 'value again')
        self.assertEqual(b.right.value, 3, 'right')
        self.assertEqual(b.left, None, 'no left')
        b = from_preorder([2,1,3])
        self.assertEqual(b.value, 2, 'value again and again')
        self.assertEqual(b.left.value, 1, 'left again')
        self.assertEqual(b.right.value, 3, 'right again')

    def test_long(self):
        b = from_preorder([10,5,3,4,7,6,8,15,13,14])
        self.assertEqual(b.value, 10, 'root value')
        self.assertEqual(b.left.value, 5, 'left child')
        self.assertEqual(b.left.left.value, 3, 'left-left')
        self.assertEqual(b.left.left.right.value, 4, 'left-left-right')
        self.assertEqual(b.left.right.value, 7, 'left-right')
        self.assertEqual(b.left.right.left.value, 6, 'left-right-left')
        self.assertEqual(b.left.right.right.value, 8, 'left-right-right')
        self.assertEqual(b.right.value, 15, 'right child')
        self.assertEqual(b.right.left.value, 13, 'right-left')
        self.assertEqual(b.right.left.right.value, 14, 'right-left-right')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test_MyBST)
    unittest.TextTestRunner(verbosity=2).run(suite)
