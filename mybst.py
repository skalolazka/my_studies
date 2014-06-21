#!/usr/bin/env python

from mystack import *

class MyBST:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def put_value(self, value):
        if self.value is None:
            self.value = value
            return self
        cur = self
        prev = cur
        which = None
        while cur is not None:
            prev = cur
            if value < cur.value:
                cur = cur.left
                which = 'left'
            else:
                cur = cur.right
                which = 'right'
        if which is not None:
            if which == 'left':
                prev.left = MyBST(value)
            else:
                prev.right = MyBST(value)

    def put_value_var2(self, value):
        cur = self
        while cur is not None:
            if value < cur.value:
                if cur.left is None:
                    cur.left = MyBST(value)
                    break
                cur = cur.left
            else:
                if cur.right is None:
                    cur.right = MyBST(value)
                    break
                cur = cur.right


def from_array(values):
    b = MyBST()
    for v in values:
        b.put_value(v)
    return b

def to_array(b):
    if b.value is None:
        return []
    cur = b
    arr = []
    s = MyStack()
    while cur is not None or not s.is_empty():
        if cur is None:
            cur = s.pop()
            arr.append(cur.value)
            cur = cur.right
        else:
            s.push(cur)
            cur = cur.left
    return arr

