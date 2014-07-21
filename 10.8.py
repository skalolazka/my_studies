#!/usr/bin/env python

# task: running median

from mynode import *

class MyNodeWithMid(MyNode):
    def __init__(self, value=None):
        MyNode.__init__(self, value)
        self.mid1 = None
        self.mid2 = None
    def median(self):
        if self.mid1 is not None:
            if self.mid2 is not None: # is even
                return (float(self.mid1.value) + float(self.mid2.value)) / 2
            else: # is odd
                return self.mid1.value
        else: # start
            return self.value

def add_head(node, value=None):
    new_node = MyNodeWithMid(value)
    if node.mid1 is not None:
        if node.mid2 is not None: # was even
            new_node.mid1 = node.mid2
        else: # was odd
            new_node.mid1 = node.mid1
            new_node.mid2 = node.mid1.next_node
    else: # start
        new_node.mid1 = node
        new_node.mid2 = new_node
    node.mid1, node.mid2 = None, None
    node.next_node = new_node
    return new_node


def running_median(node, val):
    node.add_node(val)
    return node.median()

import unittest

class MyTest(unittest.TestCase):
    def test_class(self):
        n = MyNodeWithMid(1)
        self.assertIsInstance(n, MyNodeWithMid, 'type')
        self.assertEqual(n.value, 1, 'value')
        self.assertEqual(n.next_node, None, 'next')
        self.assertEqual(n.mid1, None, 'mid1')
        self.assertEqual(n.mid2, None, 'mid2')

    def test_add(self):
        n = MyNodeWithMid(1)
        n = add_head(n, 2)
        self.assertIsInstance(n, MyNodeWithMid, 'type')
        self.assertEqual(n.value, 2, 'value')
        self.assertEqual(n.mid1.value, 1, 'mid1')
        self.assertEqual(n.mid2.value, 2, 'mid2')
        n = add_head(n, 3)
        self.assertEqual(n.value, 3, 'value')
        self.assertEqual(n.mid1.value, 2, 'mid1')
        self.assertEqual(n.mid2, None, 'mid2')
        n = add_head(n, 4)
        self.assertEqual(n.value, 4, 'value')
        self.assertEqual(n.mid1.value, 2, 'mid1')
        self.assertEqual(n.mid2.value, 3, 'mid2')
        n = add_head(n, 5)
        self.assertEqual(n.value, 5, 'value')
        self.assertEqual(n.mid1.value, 3, 'mid1')
        self.assertEqual(n.mid2, None, 'mid2')

    def test_median(self):
        n = MyNodeWithMid(1)
        n = add_head(n, 2)
        self.assertEqual(n.median(), 1.5, '2')
        n = add_head(n, 3)
        self.assertEqual(n.median(), 2, '3')
        n = add_head(n, 4)
        self.assertEqual(n.median(), 2.5, '4')
        n = add_head(n, 5)
        self.assertEqual(n.median(), 3, '5')
        n = add_head(n, 6)
        self.assertEqual(n.median(), 3.5, '6')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
