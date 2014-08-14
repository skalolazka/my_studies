#!/usr/bin/env python

import time

class MyGraph:
    def __init__(self, pairs=None):
        if pairs is None:
            pairs = []
        self.data = pairs # no check is made, I assume data is correct

    def add_vertex(self, vertex):
        if not self.has_vertex(vertex):
            self.data.append([vertex, []])

    def add_edge(self, vertex1, vertex2):
        (got1, got2) = (0, 0)
        for d in self.data:
            if d[0] == vertex1:
                got1 = 1
                if vertex2 not in d[1]:
                    d[1].append(vertex2)
                else:
                    got2 = 1
            elif vertex2 != vertex1 and d[0] == vertex2:
                got2 = 1
                if vertex1 not in d[1]:
                    d[1].append(vertex1)
                else:
                    got1 = 1
            if got1 and got2:
                break
        if not got1:
            self.data.append([vertex1, [vertex2]])
        if not got2 and vertex2 != vertex1:
            self.data.append([vertex2, [vertex1]])

    def has_vertex(self, vertex):
        for d in self.data:
            if d[0] == vertex:
                return 1
        return 0

    def has_edge(self, vertex1, vertex2):
        for d in self.data:
            if (d[0] == vertex1 and vertex2 in d[1]) or (d[0] == vertex2 and vertex1 in d[1]):
                return 1
        return 0

    def has_path(self, vertex1, vertex2, seen=None):
        if seen is None:
            seen = []
        #print 'input: v1 ', vertex1, ', v2 ', vertex2, ' seen ', seen
        #time.sleep(1)
        for d in self.data:
            if d[0] not in seen:
                if d[0] == vertex1:
                    #print 'got v1 ', vertex1
                    seen.append(d[0])
                    for dd in d[1]:
                        if dd == vertex2:
                            return 1
                    for dd in d[1]:
                        if dd not in seen:
                            res = self.has_path(dd, vertex2, seen)
                            if res:
                                return 1
                            seen.append(dd)
        #print 'returned 0'
        return 0


def is_edge(pair):
    if pair[1] is not None:
        return 1
    return 0

def edge_has_vertex(edge, vertex):
    if edge[0] == vertex or edge[1] == vertex:
        return 1
    return 0

# TODO: remove_vertex (plus all edges!), remove_edge

import unittest

class TestMyGraph(unittest.TestCase):
    def test_init(self):
        g = MyGraph()
        self.assertEqual(g.data, [], 'empty')
        p = [[1,[1]], [2,[3]],[3,[2]]]
        g = MyGraph(p)
        self.assertEqual(g.data, p, 'some init')

    def test_has_vertex(self):
        g = MyGraph([[1,[1]], [2,[3,4]], [3,[2]], [4, [2]], [5, []]])
        self.assertEqual(g.has_vertex(1), 1, '1 ok')
        self.assertEqual(g.has_vertex(2), 1, '2 ok')
        self.assertEqual(g.has_vertex(3), 1, '3 ok')
        self.assertEqual(g.has_vertex(4), 1, '4 ok')
        self.assertEqual(g.has_vertex(5), 1, '5 ok')
        self.assertEqual(g.has_vertex(7), 0, '7 not there')
        self.assertEqual(g.has_vertex(100), 0, '100 not there')

    def test_has_edge(self):
        g = MyGraph([[1,[1,2]], [2,[1,3,4]], [3,[2]], [4,[2]], [5, []]])
        self.assertEqual(g.has_edge(1,1), 1, '1,1 ok')
        self.assertEqual(g.has_edge(2,3), 1, '2,3 ok')
        self.assertEqual(g.has_edge(2,4), 1, '2,4 ok')
        self.assertEqual(g.has_edge(3,2), 1, '3,2 ok')
        self.assertEqual(g.has_edge(4,2), 1, '4,2 ok')
        self.assertEqual(g.has_edge(4,5), 0, '4,5 not there')
        self.assertEqual(g.has_edge(1,3), 0, '1,3 - path - not there')

    def test_add_vertex(self):
        g = MyGraph()
        g.add_vertex(1)
        self.assertEqual(g.data, [[1, []]], 'add 1')
        g.add_vertex(1)
        self.assertEqual(g.data, [[1, []]], '1 not added again')
        g.add_vertex(2)
        self.assertEqual(g.data, [[1, []], [2, []]], 'add 2')

    def test_add_edge(self):
        g = MyGraph()
        g.add_edge(1,1)
        self.assertEqual(g.data, [[1, [1]]], 'add 1,1')
        g.add_edge(1,1)
        self.assertEqual(g.data, [[1, [1]]], '1,1 not added again')
        g.add_edge(1,2)
        self.assertEqual(g.data, [[1, [1,2]], [2, [1]]], '1,2 ok')
        g.add_edge(2,3)
        self.assertEqual(g.data, [[1, [1,2]], [2, [1,3]], [3, [2]]], '2,3 ok')
        g.add_edge(1,3)
        self.assertEqual(g.data, [[1, [1,2,3]], [2, [1,3]], [3, [2,1]]], '1,3 ok')

    def test_has_path(self):
        g = MyGraph([[1,[1]], [2,[3,4]], [3,[2]], [4, [2,6]], [5, []], [6, [4]]])
        self.assertEqual(g.has_path(2,3), 1, '2,3 ok')
        self.assertEqual(g.has_path(1,1), 1, '1,1 ok')
        #self.assertEqual(g.has_path(2,2), 0, '2,2 not there')
# TODO: does NOT work for cycles yet
        self.assertEqual(g.has_path(2,4), 1, '2,4 ok')
        self.assertEqual(g.has_path(4,2), 1, '4,2 ok')
        self.assertEqual(g.has_path(4,5), 0, '4,5 not there')
        self.assertEqual(g.has_path(2,6), 1, '2,6 ok')
        self.assertEqual(g.has_path(6,2), 1, '6,2 ok')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMyGraph)
    unittest.TextTestRunner(verbosity=2).run(suite)
