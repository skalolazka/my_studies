#!/usr/bin/env python

# task: running median

from mynode import *

class MyNodeWithMid(MyNode):
    def __init__(self, value=None):
        MyNode.__init__(self, value)
        self.mid1 = None
        self.mid2 = None


class MyNodesWithMid(MyNodeWithMid):
    def __init__(self, value=None):
        self.start = MyNodeWithMid(value)
        self.start.mid1 = self.start

    def median(self):
        if self.start.mid2 is not None: # is even
            return (float(self.start.mid1.value) + float(self.start.mid2.value)) / 2
        else: # is odd
            return self.start.mid1.value

    def add_number(self, value=None):
        old = self.start
        self.start = MyNodeWithMid(value)
        old.next_node = self.start
        if old.mid2 is None:
            self.start.mid1 = old.mid1.next_node
            self.start.mid2 = old.mid1
        else:
            self.start.mid1 = old.mid1
        old.mid1, old.mid2 = None, None


import unittest

class MyTest(unittest.TestCase):
    def test_base_class(self):
        n = MyNodeWithMid(1)
        self.assertIsInstance(n, MyNodeWithMid, 'type')
        self.assertEqual(n.value, 1, 'value')
        self.assertEqual(n.next_node, None, 'next')
        self.assertEqual(n.mid1, None, 'mid1')
        self.assertEqual(n.mid2, None, 'mid2')

    def test_class(self):
        n = MyNodesWithMid(1)
        self.assertIsInstance(n, MyNodeWithMid, 'type base')
        self.assertIsInstance(n, MyNodesWithMid, 'type')
        self.assertEqual(n.start.value, 1, 'value')
        self.assertEqual(n.start.next_node, None, 'next')
        self.assertEqual(n.start.mid1, n.start, 'mid1')
        self.assertEqual(n.start.mid2, None, 'mid2')

    def test_add(self):
        n = MyNodesWithMid(1)
        n.add_number(2)
        self.assertIsInstance(n, MyNodeWithMid, 'type')
        self.assertEqual(n.start.value, 2, 'value')
        self.assertEqual(n.start.mid1.value, 2, 'mid1')
        self.assertEqual(n.start.mid2.value, 1, 'mid2')
        n.add_number(3)
        self.assertEqual(n.start.value, 3, 'value')
        self.assertEqual(n.start.mid1.value, 2, 'mid1')
        self.assertEqual(n.start.mid2, None, 'mid2')
        n.add_number(4)
        self.assertEqual(n.start.value, 4, 'value')
        self.assertEqual(n.start.mid1.value, 3, 'mid1')
        self.assertEqual(n.start.mid2.value, 2, 'mid2')
        n.add_number(5)
        self.assertEqual(n.start.value, 5, 'value')
        self.assertEqual(n.start.mid1.value, 3, 'mid1')
        self.assertEqual(n.start.mid2, None, 'mid2')
        n.add_number(6)
        self.assertEqual(n.start.value, 6, 'value')
        self.assertEqual(n.start.mid1.value, 4, 'mid1')
        self.assertEqual(n.start.mid2.value, 3, 'mid2')
        n.add_number(0)
        self.assertEqual(n.start.value, 0, 'value')
        self.assertEqual(n.start.mid1.value, 4, 'mid1')
        self.assertEqual(n.start.mid2, None, 'mid2')

    def test_median(self):
        n = MyNodesWithMid(1)
        n.add_number(2)
        self.assertEqual(n.median(), 1.5, '2')
        n.add_number(3)
        self.assertEqual(n.median(), 2, '3')
        n.add_number(4)
        self.assertEqual(n.median(), 2.5, '4')
        n.add_number(5)
        self.assertEqual(n.median(), 3, '5')
        n.add_number(6)
        self.assertEqual(n.median(), 3.5, '6')
        n.add_number(0)
        self.assertEqual(n.median(), 4, '7 = 0')

    def test_median2(self):
        n = MyNodesWithMid(1)
        n.add_number(1)
        n.add_number(2)
        n.add_number(0)
        n.add_number(0)
        self.assertEqual(n.median(), 2, '2')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
