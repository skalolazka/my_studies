#!/usr/bin/env python

def add(a,b):
   """
   >>> add(0, 0)
   0
   >>> add(1, 0)
   1
   >>> add(0, 1)
   1
   >>> add(1, 1)
   2
   >>> add(0, 3)
   3
   >>> add(3, 0)
   3
   >>> add(2, 3)
   5
   >>> add(10, 10)
   20
   >>> add(11, 13)
   24
   """
   result = 0
   mask = 1
   c = 0
   while mask <= a or mask <= b:
       c1 = mask & a
       c2 = mask & b
       tmp = c1 ^ c2 ^ c
       c = (c1 & c) | (c2 & c) | (c1 & c2)
       c <<= 1
       result = result | tmp
       mask <<= 1
   result = result | c

   return result

def multiply(a, b):
   """
   >>> multiply(0, 0)
   0
   >>> multiply(0, 1)
   0
   >>> multiply(1, 0)
   0
   >>> multiply(1, 1)
   1
   >>> multiply(1, 2)
   2
   >>> multiply(1, 5)
   5
   >>> multiply(5, 1)
   5
   >>> multiply(2, 3)
   6
   >>> multiply(3, 2)
   6
   >>> multiply(0, 3)
   0
   >>> multiply(11, 13)
   143
   >>> multiply(10, 100)
   1000
   >>> multiply(3, 7)
   21
   """
   result = 0
   move = 0
   while (1 << move) <= b:
       c = b & (1 << move)
       if c:
           tmp = a << move
           result = add(result, tmp)
       move += 1
       #print locals()

   return result

if __name__ == '__main__':
    import doctest
    #multiply.__doc__ = ''
    doctest.testmod(verbose = False, optionflags= doctest.REPORT_ONLY_FIRST_FAILURE)
