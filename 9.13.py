#!/usr/bin/env python

from mybintree_w_parent_9_12 import MyBinTreeWithParent

def lca_fast(n1, n2):
    if n1 == n2:
        return n1
    seen = set([n1, n2])
    while n1.parent is not None or n2.parent is not None:
        if n1.parent is not None:
            n1 = n1.parent
            if n1 in seen:
                return n1
            seen.add(n1)
        if n2.parent is not None:
            n2 = n2.parent
            if n2 in seen:
                return n2
            seen.add(n2)
    return None


import unittest

class TestLCAFast(unittest.TestCase):
    def setUp(self):
        self.t = MyBinTreeWithParent(1)
        self.t.put_left(2)
        self.t.put_right(3)
        self.t.left.put_left(4)
        self.t.left.left.put_left(5)
        self.t.left.put_right(6)
        self.t.right.put_left(7)
        self.t.right.put_right(8)

    def test_one(self):
        self.assertEqual(lca_fast(self.t,self.t), self.t, 'just one node')
        self.assertEqual(lca_fast(self.t.left,self.t.left), self.t.left, 'same nodes')

    def test_many(self):
        self.assertEqual(lca_fast(self.t.left,self.t.right), self.t, 'left and right')
        self.assertEqual(lca_fast(self.t.left.left,self.t.right), self.t, 'left.left, right')
        self.assertEqual(lca_fast(self.t.left.right,self.t.left), self.t.left, 'left.right, left')
        self.assertEqual(lca_fast(self.t.left.left.left,self.t.left.right), self.t.left, 'left.left.left, left.right')
        self.assertEqual(lca_fast(self.t.left.left.left,self.t.right), self.t, 'left.left.left, right')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLCAFast)
    unittest.TextTestRunner(verbosity=2).run(suite)
