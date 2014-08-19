#!/usr/bin/env python

# task: pins and wire, can we divide pins into left & right, wires only from left to right
# Time complexity. This is the standard task of colouring the vertices of the graph. So I'm using BFS for it. Means it is O(E).

from mygraph import MyGraph

def pins(data):
    g = MyGraph()
    for d in data:
        g.add_edge(d[0], d[1])
    return paint(g, {'white': [], 'black': []}, g.data[0])[0]

def paint(g, painted, start_vertex=None):
    if start_vertex is not None: # start with something
        painted['white'].append(start_vertex[0])
        for dd in start_vertex[1]:
            painted['black'].append(dd)
        for dd in start_vertex[1]:
            (res, painted) = paint(g, painted)
            if res == 0:
                return (res, painted)
    else:
        for d in g.data:
            color = None
            if d[0] in painted['white']:
                color = 'black'
                opposite = 'white'
            if d[0] in painted['black']:
                color = 'white'
                opposite = 'black'
            if color is not None: # have painted this one - paint children
                new = 0
                for dd in d[1]:
                    if dd in painted[opposite]:
                        return (False, painted)
                    if dd not in painted[color]:
                        new = 1
                        painted[color].append(dd)
                if new != 0: # have at least something to paint here
                    for dd in d[1]:
                        (res, painted) = paint(g, painted)
                        if res == 0:
                            return (res, painted)
    for d in g.data: # check if there are not painted vertices yet
    # means the graph has more than one connected component
        if d[0] not in painted['white'] and d[0] not in painted['black']:
            paint(g, painted, d)
    return (True, painted)


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

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPins)
    unittest.TextTestRunner(verbosity=2).run(suite)
