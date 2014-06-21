#!/usr/bin/env python

class MyStack:
    def __init__(self, values=None):
        if values is None or len(values) == 0:
            self.values = []
            self.pointer = None
        else:
            self.values = values
            self.pointer = len(values) - 1

    def push(self, value):
        if self.pointer is None:
            self.pointer = -1
        if self.pointer == len(self.values) - 1:
            self.values.append(value)
        else:
            self.values[self.pointer+1] = value
        self.pointer += 1

    def pop(self):
        if self.pointer is None:
            return None
        value = self.values[self.pointer]
        if self.pointer == 0:
            self.pointer = None
        else:
            self.pointer -= 1
        return value

    def max(self):
        if self.pointer is None:
            return None
        m = None
        backup = MyStack()
        while self.pointer is not None:
            val = self.pop()
            if val > m:
                m = val
            backup.push(val)
        b = backup.pop()
        while b is not None:
            self.push(b)
            b = backup.pop()
        return m

    def to_array(self):
        if self.pointer is None:
            return []
        return self.values[0:self.pointer+1]

    def is_empty(self):
        if self.pointer is None:
            return True
        else:
            return False
