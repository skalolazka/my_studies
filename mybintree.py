#!/usr/bin/env python

from Queue import Queue, Empty # ok, so there was no task to implement a queue in Python!

class MyBinTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def put_left(self, value):
        if isinstance(value, MyBinTree): # let's leave it this simple for now
            self.left = value
        else:
            self.left = MyBinTree(value)

    def put_right(self, value):
        if isinstance(value, MyBinTree): # let's leave it this simple for now
            self.right = value
        else:
            self.right = MyBinTree(value)

    def array_by_levels(self):
        if self.value is None:
            return []
        cur = self
        q = Queue()
        res = []
        while cur is not None or not q.empty():
            res.append(cur.value)
            if cur.left is not None:
                q.put(cur.left)
            if cur.right is not None:
                q.put(cur.right)
            try:
                cur = q.get_nowait()
            except Empty:
                break
        return res
