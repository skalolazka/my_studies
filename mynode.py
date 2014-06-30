#!/usr/bin/env python

class MyNode:
    def __init__(self, value=None):
        self.value = value
        self.next_node = None

def to_array(first):
    values = []
    while first is not None:
        values.append(first.value)
        first = first.next_node
    return values

def from_array(arr):
    ll = MyNode()
    cur = ll
    for a in arr:
        new_node = MyNode(a)
        cur.next_node = new_node
        cur = new_node
    return ll.next_node

def length(first):
    length = 0
    while first.next_node is not None:
        length += 1
        first = first.next_node
    return length

import unittest

class MyTest(unittest.TestCase):
    def test_from_array_empty(self):
        n = from_array([])
        self.assertEqual(n, None, 'None')

    def test_from_array_empty(self):
        n = from_array([None])
        self.assertIsInstance(n, MyNode, 'type')
        self.assertEqual(n.value, None, 'value')
        self.assertEqual(n.next_node, None, 'next')

    def test_from_array_one(self):
        n = from_array([1])
        self.assertIsInstance(n, MyNode, 'type')
        self.assertEqual(n.value, 1, 'value')
        self.assertEqual(n.next_node, None, 'next')

    def test_from_array_many(self):
        n = from_array([4,5,3])
        self.assertIsInstance(n, MyNode, 'type')
        self.assertEqual(n.value, 4, 'value')
        n = n.next_node
        self.assertEqual(n.value, 5, 'next value')
        n = n.next_node
        self.assertEqual(n.value, 3, 'last value')
        self.assertEqual(n.next_node, None, 'end')

    def test_to_array_one(self):
        a = to_array(MyNode(1))
        self.assertIsInstance(a, list, 'type')
        self.assertEqual(a[0], 1, 'value')
        self.assertEqual(len(a), 1, 'length')

    def test_to_array_many(self):
        n = MyNode(5)
        n.next_node = MyNode(3)
        n.next_node.next_node = MyNode(4)
        a = to_array(n)
        self.assertIsInstance(a, list, 'type')
        self.assertEqual(a[0], 5, 'value 0')
        self.assertEqual(a[1], 3, 'value 1')
        self.assertEqual(a[2], 4, 'value 2')
        self.assertEqual(len(a), 3, 'length')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
