#!/usr/bin/env python

# task: stack with max

from mynode import *
from collections import deque

class MyStack:
    def __init__(self, values=None):
        if values is None or len(values) == 0:
            self.for_max = []
            self.values = []
            self.pointer = None
        else:
            self.values = [None for v in xrange(0, len(values))]#values
            self.for_max = deque()
            self.pointer = None
            for value in values:
                self.push(value)

    def push(self, value):
        if self.pointer is None:
            self.pointer = -1
        if self.pointer == len(self.values) - 1:
            self.values.append(value)
        else:
            self.values[self.pointer+1] = value
        self.for_max.append(max(self.max(), value))
        self.pointer += 1

    def pop(self):
        if self.pointer is None:
            return None
        value = self.values[self.pointer]
        if self.pointer == 0:
            self.pointer = None
        else:
            self.pointer -= 1
        self.for_max.pop()
        return value

    def max(self):
        if self.for_max:
            return self.for_max[-1]
        else:
            return None

    def to_array(self):
        if self.pointer is None:
            return []
        return self.values[0:self.pointer+1]

    def is_empty(self):
        if self.pointer is None:
            return True
        else:
            return False

import unittest

class MyStackTest(unittest.TestCase):
    def test_is_empty(self):
        s = MyStack()
        self.assertEqual(s.is_empty(), True, 'empty')
        s = MyStack([1])
        self.assertEqual(s.is_empty(), False, 'not empty')
        s.pop()
        self.assertEqual(s.is_empty(), True, 'empty now')

    def test_empty(self):
        s = MyStack()
        self.assertIsInstance(s, MyStack, 'instance')
        self.assertEqual(s.pop(), None, 'nothing in there')
        self.assertEqual(s.pop(), None, 'nothing in there again')
        s.push(1)
        self.assertEqual(s.pop(), 1, 'added one')
        s.push(2)
        s.push(3)
        self.assertEqual(s.pop(), 3, 'added more')
        self.assertEqual(s.pop(), 2, 'pop more')
        self.assertEqual(s.pop(), None, 'pop again')
        self.assertEqual(s.pop(), None, 'pop again and again')

    def test_full(self):
        s = MyStack([1,2,3,4])
        self.assertEqual(s.pop(), 4, 'initialized')
        self.assertEqual(s.pop(), 3, "more poppin'")
        self.assertEqual(s.pop(), 2, "and more poppin'")
        self.assertEqual(s.pop(), 1, "and even more poppin'")
        self.assertEqual(s.pop(), None, "none left")

    def test_to_array(self):
        s = MyStack([])
        self.assertEqual(s.to_array(), [], 'to_array empty')
        s = MyStack([1,2,3,4])
        self.assertEqual(s.to_array(), [1,2,3,4], 'to_array with new')
        s.pop()
        self.assertEqual(s.to_array(), [1,2,3], 'to_array after pop')
        s.push(5)
        self.assertEqual(s.to_array(), [1,2,3,5], 'to_array after pop')

    def test_max(self):
        s = MyStack([1,2,5,4,0])
        self.assertEqual(s.max(), 5, 'max for long')
        self.assertEqual(s.to_array(), [1,2,5,4,0], 's not changed')
        s = MyStack([1,2,5,4])
        self.assertEqual(s.max(), 5, 'max for long again')
        s.pop()
        self.assertEqual(s.max(), 5, 'max still same after pop of non-max')
        s.pop()
        self.assertEqual(s.max(), 2, 'max changed after pop')
        s.push(6)
        self.assertEqual(s.max(), 6, 'max changed after push')
        s = MyStack([])
        self.assertEqual(s.max(), None, 'max for empty')
        s.push(2)
        self.assertEqual(s.max(), 2, 'max initialized')
        s.pop()
        self.assertEqual(s.max(), None, 'max for empty now')
        s = MyStack([5,4,1,2])
        self.assertEqual(s.max(), 5, 'max in the bottom')
        self.assertEqual(s.to_array(), [5,4,1,2], 's not changed now too')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyStackTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
