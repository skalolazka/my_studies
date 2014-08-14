#!/usr/bin/env python

# task: can all equations be satisfied simultaneously

from mygraph import MyGraph

def satisfy(pairs):
    if pairs is None or pairs == [] or len(pairs) == 1:
        return 1
    (equal, not_eq) = (MyGraph(), MyGraph())
    (arr_eq, arr_ne) = ([], [])
    # [a,b] => "a = b", [a,b,1] => "a != b"
    for p in pairs:
        if len(p) > 2: # not equal
            not_eq.add_edge(p[0], p[1])
            arr_ne.append([p[0], p[1]])
        else: # equal
            equal.add_edge(p[0], p[1])
            arr_eq.append([p[0], p[1]])
    check = arr_eq if len(arr_eq) < len(arr_ne) else arr_ne
    for p in check:
        if equal.has_path(p[0], p[1]) and not_eq.has_path(p[0], p[1]):
            return 0
    return 1

import unittest

class TestSatisfy(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(satisfy(None), 1, 'None ok')
        self.assertEqual(satisfy([]), 1, '[] ok')

    def test_simple(self):
        self.assertEqual(satisfy([[1,1]]), 1, 'one ok')
        self.assertEqual(satisfy([[1,2], [2,3], [4,5]]), 1, 'just eq ok')

    def test_more(self):
        self.assertEqual(satisfy([[1,2], [3,4,1]]), 1, 'ok')
        self.assertEqual(satisfy([[1,2], [1,2,1]]), 0, 'not ok')
        self.assertEqual(satisfy([[1,2], [2,1,1]]), 0, 'not ok swapped')
        self.assertEqual(satisfy([[1,2], [2,3], [1,3,1]]), 0, 'not ok for longer')
        self.assertEqual(satisfy([[1,2], [2,3], [3,4], [5,6], [1,4,1]]), 0, 'not ok for even longer')
        self.assertEqual(satisfy([[1,2], [2,3], [3,4], [5,6], [1,5,1]]), 1, 'ok for longer')

    def test_a_lot(self):
        self.assertEqual(satisfy([[1,2], [2,3], [3,4], [5,6], [1,5,1], [1,6,1], [1,7]]), 1, 'ok')
        self.assertEqual(satisfy([[1,2], [2,3], [3,4], [5,6], [1,5,1], [1,6,1], [1,7], [2,7,1]]), 0, 'not ok')

    def test_same(self):
        self.assertEqual(satisfy([[1,1], [1,1,1]]), 0, 'same not ok')
        self.assertEqual(satisfy([[1,2], [2,3], [1,3,1]]), 0, 'not ok')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSatisfy)
    unittest.TextTestRunner(verbosity=2).run(suite)
