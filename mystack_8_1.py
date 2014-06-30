#!/usr/bin/env python

from mynode import *

class MyStack:
    def __init__(self, values=None):
        self.for_max = None
        if values is None or len(values) == 0:
            self.values = []
            self.pointer = None
        else:
            self.values = values
            self.pointer = len(values) - 1
            for value in values:
                self.insert_for_max(value)

    def push(self, value):
        if self.pointer is None:
            self.pointer = -1
        if self.pointer == len(self.values) - 1:
            self.values.append(value)
        else:
            self.values[self.pointer+1] = value
        self.pointer += 1
        self.insert_for_max(value)

    def insert_for_max(self, value):
        print 'received v ', value
        if self.for_max is None:
            self.for_max = MyNode(value)
            return
        if self.for_max.value > value:
            first = MyNode(value)
            first.next_node = self.for_max
            print 'in start ', to_array(self.for_max)
            return
        print 'before: ', to_array(self.for_max)
        ptr = self.for_max
        prev = MyNode()
        first = prev
        inserted = 0
        while ptr is not None:
            if prev.value <= value and ptr.value >= value:
                inserted = 1
                print 'OOOOOOOKKKKKKKK'
                prev.next_node = MyNode(value)
                prev.next_node.next_node = ptr
                break
            prev = ptr
            ptr = ptr.next_node
        if not inserted:
            print 'not inserted ', prev.value
            prev.next_node = MyNode(value)
            print 'prev now ', to_array(prev)
        self.for_max = first.next_node
        print 'inserted ', value, ' now ', to_array(self.for_max)

    def pop(self):
        if self.pointer is None:
            return None
        value = self.values[self.pointer]
        if self.pointer == 0:
            self.pointer = None
        else:
            self.pointer -= 1
        return value

    def max(self):
        if self.pointer is None:
            return None
        m = None
        backup = MyStack()
        while self.pointer is not None:
            val = self.pop()
            if val > m:
                m = val
            backup.push(val)
        b = backup.pop()
        while b is not None:
            self.push(b)
            b = backup.pop()
        return m

    def fast_max(self):
        pass

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
    @unittest.skip('later')
    def test_is_empty(self):
        s = MyStack()
        self.assertEqual(s.is_empty(), True, 'empty')
        s = MyStack([1])
        self.assertEqual(s.is_empty(), False, 'not empty')
        s.pop()
        self.assertEqual(s.is_empty(), True, 'empty now')

    @unittest.skip('later')
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

    @unittest.skip('later')
    def test_full(self):
        s = MyStack([1,2,3,4])
        self.assertEqual(s.pop(), 4, 'initialized')
        self.assertEqual(s.pop(), 3, "more poppin'")
        self.assertEqual(s.pop(), 2, "and more poppin'")
        self.assertEqual(s.pop(), 1, "and even more poppin'")
        self.assertEqual(s.pop(), None, "none left")

    @unittest.skip('later')
    def test_to_array(self):
        s = MyStack([])
        self.assertEqual(s.to_array(), [], 'to_array empty')
        s = MyStack([1,2,3,4])
        self.assertEqual(s.to_array(), [1,2,3,4], 'to_array with new')
        s.pop()
        self.assertEqual(s.to_array(), [1,2,3], 'to_array after pop')
        s.push(5)
        self.assertEqual(s.to_array(), [1,2,3,5], 'to_array after pop')

    @unittest.skip('later')
    def test_max(self):
        s = MyStack([1,2,5,4,0])
        self.assertEqual(s.max(), 5, 'max for long')
        self.assertEqual(s.to_array(), [1,2,5,4,0], 's not changed')
        s = MyStack([])
        self.assertEqual(s.max(), None, 'max for empty')
        s = MyStack([5,4,1,2])
        self.assertEqual(s.max(), 5, 'max in the bottom')
        self.assertEqual(s.to_array(), [5,4,1,2], 's not changed now too')

    def test_fast_max(self):
        s = MyStack([1,2,5,4,6,0])


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyStackTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
