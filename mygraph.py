#!/usr/bin/env python

from collections import defaultdict, deque

class MyGraph:
    def __init__(self, pairs=None):
        self.data = defaultdict(set)
        if pairs is None:
            pairs = []
        for v1, adj_list in pairs:
            self.add_vertex(v1)
            for v2 in adj_list:
                self.add_edge(v1, v2)

    def add_vertex(self, vertex):
        self.data[vertex]

    def add_edge(self, vertex1, vertex2):
        self.data[vertex1].add(vertex2)
        self.data[vertex2].add(vertex1)

    def has_vertex(self, vertex):
        return self.data.get(vertex) is not None

    def has_edge(self, vertex1, vertex2):
        return vertex2 in self.data.get(vertex1, [])

    def adj_vertices(self, vertex):
        return self.data.get(vertex)

    def has_path(self, vertex1, vertex2):
        seen = set()
        q = deque([vertex1])
        add_next = q.append
        # add_next = q.appendleft

        while q:
            v = q.popleft()
            seen.add(v)
            for out in self.adj_vertices(v):
                if out not in seen:
                    add_next(out)
        return vertex2 in seen

    def vertices(self):
        return self.data.keys()

# TODO: remove_vertex (plus all edges!), remove_edge

import unittest

class TestMyGraph(unittest.TestCase):
    def test_init(self):
        g = MyGraph()
        #self.assertEqual(g.data, defaultdict(set), 'empty')
        self.assertFalse(g.data, 'empty')
        p = [[1,[1]], [2,[3]],[3,[2]]]
        g = MyGraph(p)
        self.assertTrue(g.data, 'not empty')

    def test_has_vertex(self):
        g = MyGraph([[1,[1]], [2,[3,4]], [3,[2]], [4, [2]], [5, []]])
        self.assertTrue(g.has_vertex(1), '1 ok')
        self.assertTrue(g.has_vertex(2), '2 ok')
        self.assertTrue(g.has_vertex(3), '3 ok')
        self.assertTrue(g.has_vertex(4), '4 ok')
        self.assertTrue(g.has_vertex(5), '5 ok')
        self.assertFalse(g.has_vertex(7), '7 not there')
        self.assertFalse(g.has_vertex(100), '100 not there')

    def test_has_edge(self):
        g = MyGraph([[1,[1,2]], [2,[1,3,4]], [3,[2]], [4,[2]], [5, []]])
        self.assertTrue(g.has_edge(1,1), '1,1 ok')
        self.assertTrue(g.has_edge(2,3), '2,3 ok')
        self.assertTrue(g.has_edge(2,4), '2,4 ok')
        self.assertTrue(g.has_edge(3,2), '3,2 ok')
        self.assertTrue(g.has_edge(4,2), '4,2 ok')
        self.assertFalse(g.has_edge(4,5), '4,5 not there')
        self.assertFalse(g.has_edge(1,3), '1,3 - path - not there')

    def test_add_vertex(self):
        g = MyGraph()
        g.add_vertex(1)
        self.assertTrue(g.has_vertex(1), 'add 1')        
        self.assertItemsEqual(g.vertices(), [1], 'add 1, test vertices')
        g.add_vertex(1)
        self.assertTrue(g.has_vertex(1), '1 not added again')
        self.assertItemsEqual(g.vertices(), [1], 'add 1 again, test vertices')
        self.assertFalse(g.has_vertex(2), 'doesn\'t have 2')
        g.add_vertex(2)
        self.assertTrue(g.has_vertex(2), 'add 2')
        self.assertItemsEqual(g.vertices(), [1, 2], 'add 2, test vertices')

    def test_add_edge(self):
        g = MyGraph()
        g.add_edge(1,1)
        self.assertTrue(g.has_edge(1,1), 'add 1,1')
        g.add_edge(1,1)
        self.assertItemsEqual(g.adj_vertices(1), [1], '1,1 not added again')
        g.add_edge(1,2)
        self.assertItemsEqual(g.adj_vertices(1), [1, 2], '1,2 ok for 1')
        self.assertItemsEqual(g.adj_vertices(2), [1], '1,2 ok for 2')

        g.add_edge(2,3)
        self.assertItemsEqual(g.adj_vertices(1), [1, 2], '2,3 ok')
        self.assertItemsEqual(g.adj_vertices(2), [1, 3], '2,3 ok')
        self.assertItemsEqual(g.adj_vertices(3), [2], '2,3 ok')

        g.add_edge(1,3)
        self.assertItemsEqual(g.adj_vertices(1), [1, 2,3], '1,3 ok')
        self.assertItemsEqual(g.adj_vertices(2), [1, 3], '1,3 ok')
        self.assertItemsEqual(g.adj_vertices(3), [1, 2], '1,3 ok')


    def test_has_path(self):
        g = MyGraph([[1,[1]], [2,[3,4,7]], [3,[2]], [4, [2,6,8]], [5, []], [6, [4]], [7,[2,8]], [8,[4,7]]])
        self.assertTrue(g.has_path(2,3), '2,3 ok')
        self.assertTrue(g.has_path(1,1), '1,1 ok')
        self.assertTrue(g.has_path(2,2), '2,2 ok')
        self.assertTrue(g.has_path(2,4), '2,4 ok')
        self.assertTrue(g.has_path(4,2), '4,2 ok')
        self.assertTrue(g.has_path(2,8), '2,8 ok')
        self.assertFalse(g.has_path(4,5), '4,5 not there')
        self.assertTrue(g.has_path(2,6), '2,6 ok')
        self.assertTrue(g.has_path(6,2), '6,2 ok')

    def test_adj_vertices(self):
        g = MyGraph([[1,[1,2]], [2,[1,3,4]], [3,[2]], [4,[2]], [5, []]])
        self.assertItemsEqual(g.adj_vertices(1), [1, 2], 'adj_vertices(1) ok')
        self.assertItemsEqual(g.adj_vertices(2), [1, 3, 4], 'adj_vertices(2) ok')
        self.assertItemsEqual(g.adj_vertices(3), [2], 'adj_vertices(3) ok')
        self.assertItemsEqual(g.adj_vertices(4), [2], 'adj_vertices(4) ok')
        self.assertItemsEqual(g.adj_vertices(5), [], 'adj_vertices(5) ok')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMyGraph)
    unittest.TextTestRunner(verbosity=2).run(suite)
