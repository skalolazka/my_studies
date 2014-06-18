#!/usr/bin/env python

class MyNode:
    def __init__(self, value=None):
        self.value = value
        self.next_node = None

def to_array(first):
    values = []
    while first is not None:
        values.append(first.value)
        first = first.next_node
    return values

def from_array(arr):
    if len(arr) == 0:
        return None
    ll = MyNode(arr[0])
    cur = ll
    for a in arr[1:]:
        new_node = MyNode(a)
	cur.next_node = new_node
	cur = new_node
    return ll
