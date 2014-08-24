#!/usr/bin/env python

# task: pins and wire, can we divide pins into left & right, wires only from left to right
# Time complexity. This is the standard task of colouring the vertices of the graph. So I'm using BFS for it. Means it is O(E).

from mygraph import MyGraph

def pins(data):
    g = MyGraph()
    for d in data:
        g.add_edge(d[0], d[1])

    visited = set()
    for v in g.vertices():
        if v not in visited:
            res = paint(g, v)
            if res is None:
                return False
            visited.update(res)
    return True

def paint(g, start_vertex):
    cur_q = [start_vertex]
    next_q = []
    cur_col = set()
    next_col = set()

    while cur_q:
        for v in cur_q:
            if v in next_col:
                return None
            cur_col.add(v)
            for adj in g.adj_vertices(v):
                if adj not in next_col:
                    next_q.append(adj)
        cur_col, next_col = next_col, cur_col
        cur_q, next_q = next_q, []

    return cur_col.union(next_col)    

import unittest

class TestPins(unittest.TestCase):
    def test_small(self):
        self.assertTrue(pins([[1,2],[1,3]]), 'ok')
        self.assertTrue(pins([[1,2],[2,3]]), 'ok again')
        self.assertFalse(pins([[1,2],[2,3],[1,3]]), 'not ok')

    def test_big(self):
        self.assertTrue(pins([[1,2],[1,4],[1,8],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[7,2]]), 'big ok')

    def test_big_no(self):
        self.assertFalse(pins([[1,2],[1,4],[1,8],[4,5],[5,7],[7,8],[7,2]]), 'big not ok')

    def test_two_components(self):
        self.assertFalse(pins([[1,2],[2,3],[3,4],[1,3],[5,6],[6,7],[5,7]]), 'two components not ok')
        self.assertTrue(pins([[1,2],[2,3],[3,4],[1,4],[5,6],[6,7],[7,8],[8,9],[5,8]]), 'two components ok')

    def test_two_components2(self):
        self.assertFalse(pins([[1,2], [3,4], [4,5], [3,5]]), 'two components not ok')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPins)
    unittest.TextTestRunner(verbosity=2).run(suite)
