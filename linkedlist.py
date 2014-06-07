#!/usr/bin/env python

class Node:
    def __init__(self, val=None):
        self.value = val
        self.next_node = None
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.value == other.value and \
            ((self.next_node is not None and other.next_node is not None) or (self.next_node is None and other.next_node is None)):
                return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

class LinkedList:
    first, last = None, None
    def __init__(self, values=[]):
        for val in values:
            self.add_node(val)
    def add_node(self, val):
        if self.last == None:
            self.last = Node(val)
            self.first = self.last
        else:
            new_node = Node(val)
            self.last.next_node = new_node
            self.last = new_node

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            iter1, iter2 = self.first, other.first
            while 1:
                if iter1 is None and iter2 is None:
                    break
                if iter1 != iter2 or iter1 is None or iter2 is None:
                    return False
                iter1, iter2 = iter1.next_node, iter2.next_node
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
