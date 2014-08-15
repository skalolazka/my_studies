#!/usr/bin/env python

# task: pins and wire, can we divide pins into left & right, wires only from left to right

from mygraph import MyGraph

delay = 2 # that's the 60 minutes between flights, just to make it easier

def flight(timetable, c_from, c_to, start, current=0, min_t=None): # city_from, city_to, start time, current time, minimum time
    if c_from == c_to:
        return 0
    for f in timetable:
        if f[0] == c_from and f[2] >= start: # found originating city and proper time
            wait = f[2] - start
            current = current + f[3] - f[2] + wait
            if f[1] == c_to: # reached end point
                if min_t is None or current < min_t:
                    min_t = current
            else:
                res = flight(timetable, f[1], c_to, f[3] + delay, 0, None)
                if res is not None and (min_t is None or res + current + delay < min_t):
                    min_t = res + current + delay
            current = 0
    return min_t

import unittest

class TestFlight(unittest.TestCase):
    def setUp(self):
        self.timetable = [
            ['a','x',0,11],
            ['a','c',0,9],
            ['a','b',1,2],
            ['b','c',4,7],
            ['b','d',10,20],
            ['c','d',2,5],
            ['a','e',0,1],
            ['q','w',0,1],
            ['w','r',4,9],
            ['w','r',5,6],
        ]

    @unittest.skip('ok')
    def test_nothing(self):
        self.assertEqual(flight(self.timetable, 't', 'b', 0), None, 'city not found')
        self.assertEqual(flight(self.timetable, 'a', 't', 0), None, 'end city not found')
        self.assertEqual(flight(self.timetable, 'a', 'e', 1), None, 'just a line - but too late')

    @unittest.skip('ok')
    def test_easy(self):
        self.assertEqual(flight(self.timetable, 'a', 'x', 0), 11, 'just a line')
        self.assertEqual(flight(self.timetable, 'a', 'e', 0), 1, 'just a line again')

    def test_more(self):
        self.assertEqual(flight(self.timetable, 'a', 'c', 0), 7, 'two instead of one')
        self.assertEqual(flight(self.timetable, 'q', 'r', 0), 6, 'two instead of one')
        self.assertEqual(flight(self.timetable, 'b', 'd', 2), 18, 'long wait')
        self.assertEqual(flight(self.timetable, 'a', 'd', 0), 20, 'long way, two flights')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestFlight)
    unittest.TextTestRunner(verbosity=2).run(suite)
