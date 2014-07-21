#!/usr/bin/env python

# task: common elems of two sorted arrays without duplicates

def common_elems(a, b):
    if a is None or b is None:
        return None
    i, j = 0, 0
    c = []
    prev = None
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            i += 1
            prev = None
        elif a[i] > b[j]:
            j += 1
            prev = None
        else: # equal
            if prev is None or prev != a[i]:
                c.append(a[i])
            prev = a[i]
            i += 1
            j += 1
    return c


import unittest

class MyTest(unittest.TestCase):
    def test_none(self):
       self.assertEqual(common_elems(None, None), None, 'None')

    def test_empty(self):
       self.assertEqual(common_elems([], []), [], 'empty')
       self.assertEqual(common_elems([1,2], []), [], 'one empty')
       self.assertEqual(common_elems([1,3,4,6], [2,5,7,8,9]), [], 'no same elems')

    def test_some(self):
       self.assertEqual(common_elems([1], [1]), [1], '1')
       self.assertEqual(common_elems([1], [1,2,3]), [1], '2')
       self.assertEqual(common_elems([2], [1,2,3]), [2], '3')
       self.assertEqual(common_elems([1,2,3], [1,2,3]), [1,2,3], '4')
       self.assertEqual(common_elems([2,2], [2,2]), [2], '5')
       self.assertEqual(common_elems([1,2,2,2,3,4,5,6,7,7], [2,2,2,4,7,8,8,9]), [2,4,7], '6')
       self.assertEqual(common_elems([1,1,1,2,2,3,5,5,6,8,9,9,9], [1,1,8,9,9,]), [1,8,9], '7')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
