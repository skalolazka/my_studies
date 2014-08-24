#!/usr/bin/env python

# task: can all equations be satisfied simultaneously
# Time complexity. I build two graphs out of the equations: let the variables be vertices and one graph is for the equalities
# (draw an edge between two variables when you see an equasion with them) and the other is for the inequalities accordingly.
# I use the mygraph library I have written, the function 'has_path' there is a DFS, so it's O(E).

from mygraph import MyGraph

def satisfy(pairs_eq, pairs_ne):
    if pairs_eq is None or pairs_eq == [] or pairs_ne is None or pairs_ne == []:
        return True
    (equal, not_eq) = (MyGraph(), MyGraph())
    (arr_eq, arr_ne) = ([], [])
    # [a,b] => "a = b", [a,b,1] => "a != b"
    for p in pairs_eq:
        equal.add_edge(p[0], p[1])
        arr_eq.append([p[0], p[1]])
    for p in pairs_ne:
        not_eq.add_edge(p[0], p[1])
        arr_ne.append([p[0], p[1]])
    check = arr_eq if len(arr_eq) < len(arr_ne) else arr_ne
    for p in check:
        if equal.has_path(p[0], p[1]) and not_eq.has_path(p[0], p[1]):
            return False
    return True

import unittest

class TestSatisfy(unittest.TestCase):
    def test_empty(self):
        self.assertTrue(satisfy(None, None), 'None ok')
        self.assertTrue(satisfy([], []), '[] ok')

    def test_simple(self):
        self.assertTrue(satisfy([[1,1]], []), 'one ok')
        self.assertTrue(satisfy([[1,2], [2,3], [4,5]], []), 'just eq ok')

    def test_more(self):
        self.assertTrue(satisfy([[1,2]], [[3,4,]]), 'ok')
        self.assertFalse(satisfy([[1,2]], [[1,2,]]), 'not ok')
        self.assertFalse(satisfy([[1,2]], [[2,1]]), 'not ok swapped')
        self.assertFalse(satisfy([[1,2], [2,3]], [[1,3]]), 'not ok for longer')
        self.assertFalse(satisfy([[1,2], [2,3], [3,4], [5,6]], [[1,4]]), 'not ok for even longer')
        self.assertTrue(satisfy([[1,2], [2,3], [3,4], [5,6]], [[1,5]]), 'ok for longer')

    def test_a_lot(self):
        self.assertTrue(satisfy([[1,2], [2,3], [3,4], [5,6], [1,7]], [[1,5], [1,6]]), 'ok')
        self.assertFalse(satisfy([[1,2], [2,3], [3,4], [5,6], [1,7]], [[1,5], [1,6], [2,7]]), 'not ok')

    def test_same(self):
        self.assertFalse(satisfy([[1,1]], [[1,1]]), 'same not ok')
        self.assertFalse(satisfy([[1,2], [2,3]], [[1,3]]), 'not ok')

    def test_dizzy(self):
        self.assertFalse(satisfy([[1,2]], [[1,3],[2,3]]), 'not ok')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSatisfy)
    unittest.TextTestRunner(verbosity=2).run(suite)
