#!/usr/bin/env python

# task: maze, find path. 0 - empty, 1 - filled
# Time complexity: think of a maze as a graph where each empty square (0 in my implementation) is a vertex,
# and two vertexes have an edge if they share a side. So I'm using DFS here. Means that it's O(E).

def maze_path(maze, start=None, end=None, seen=None):
    # I believe input is a proper matrix
    if start is None:
        start = [0, 0]
    if end is None:
        end = [len(maze)-1, len(maze[-1])-1]
    if seen is None:
        seen = [start]
    if maze[start[0]][start[1]] == 1 or maze[end[0]][end[1]] == 1:
        return (0, seen)
    if start == end:
        return (1, seen)
    adjacent = []
    if start[0] > 0 and maze[start[0]-1][start[1]] == 0 and [start[0]-1, start[1]] not in seen:
        adjacent.append([start[0]-1, start[1]])
    if start[0] < len(maze)-1 and maze[start[0]+1][start[1]] == 0 and [start[0]+1, start[1]] not in seen:
        adjacent.append([start[0]+1, start[1]])
    if start[1] > 0 and maze[start[0]][start[1]-1] == 0 and [start[0], start[1]-1] not in seen:
        adjacent.append([start[0], start[1]-1])
    if start[1] < len(maze[0])-1 and maze[start[0]][start[1]+1] == 0 and [start[0], start[1]+1] not in seen:
        adjacent.append([start[0], start[1]+1])
    for a in adjacent:
        seen.append(a)
        (result, seen) = maze_path(maze, a, end, seen)
        if result:
            return (result, seen)
    return (0, seen)

import unittest

class TestMaze(unittest.TestCase):
    def test_small(self):
        self.assertEqual(maze_path([[1]])[0], 0, 'very small, no')
        self.assertEqual(maze_path([[1,1],[1,1]])[0], 0, 'small, no')
        self.assertEqual(maze_path([[1,1,1],[1,1,1]])[0], 0, 'bit bigger, no')
        self.assertEqual(maze_path([[0,0,0],[0,0,0]])[0], 1, 'bit bigger, yes')

    def test_bigger(self):
        self.assertEqual(maze_path([[0,1,1],[0,0,0],[1,1,0]])[0], 1, 'got path')
        self.assertEqual(maze_path([[0,1,1],[0,1,0],[1,1,0]])[0], 0, 'no path')

    def test_big(self):
        self.assertEqual(maze_path([
            [0,1,1,0,0,0,1],
            [0,0,1,0,1,0,0],
            [1,0,0,0,1,1,0],
            [0,0,1,0,0,1,0]
        ])[0], 1, 'got path')

    def test_big_none(self):
        self.assertEqual(maze_path([
            [0,1,0,0,0,0,1],
            [0,0,1,0,1,0,0],
            [1,0,0,1,1,1,0],
            [0,0,1,0,0,1,0]
        ])[0], 0, 'no path')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMaze)
    unittest.TextTestRunner(verbosity=2).run(suite)
