#!/usr/bin/env python

# task: common elems of two sorted arrays without duplicates

def common_elems(a, b):
    i, j = 0, 0
    c = set()
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1
        else: # equal
            c.add(a[i])
            i += 1
            j += 1
    return c


import unittest

class MyTest(unittest.TestCase):
    def test_empty(self):
       self.assertEqual(common_elems([], []), set([]), 'empty')
       self.assertEqual(common_elems([1,2], []), set([]), 'one empty')
       self.assertEqual(common_elems([1,3,4,6], [2,5,7,8,9]), set([]), 'no same elems')

    def test_some(self):
       self.assertEqual(common_elems([1], [1]), set([1]), '1')
       self.assertEqual(common_elems([1], [1,2,3]), set([1]), '2')
       self.assertEqual(common_elems([2], [1,2,3]), set([2]), '3')
       self.assertEqual(common_elems([1,2,3], [1,2,3]), set([1,2,3]), '4')
       self.assertEqual(common_elems([2,2], [2,2]), set([2]), '5')
       self.assertEqual(common_elems([1,2,2,2,3,4,5,6,7,7], [2,2,2,4,7,8,8,9]), set([2,4,7]), '6')
       self.assertEqual(common_elems([1,1,1,2,2,3,5,5,6,8,9,9,9], [1,1,8,9,9,]), set([1,8,9]), '7')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
