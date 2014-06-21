#!/usr/bin/env python

import unittest
from mystack import MyStack

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
        s = MyStack([])
        self.assertEqual(s.max(), None, 'max for empty')
        s = MyStack([5,4,1,2])
        self.assertEqual(s.max(), 5, 'max in the bottom')
        self.assertEqual(s.to_array(), [5,4,1,2], 's not changed now too')



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyStackTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
