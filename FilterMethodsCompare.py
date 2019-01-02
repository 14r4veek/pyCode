# -*- coding: utf-8 -*-

from random import randint
import timeit

data = [randint(-10, 10) for _ in xrange(10)]

def CommReNeg():
    res = []
    for x in data:
        if x >= 0:
            res.append(x)
    print res

def FiltReNeg():
    print filter(lambda x: x >= 0, data)

def ListReNeg():
    print [x for x in data if x >= 0]

if __name__ == '__main__':
    print (timeit.timeit("CommReNeg()", setup="from __main__ import CommReNeg", number=1))
    print (timeit.timeit("FiltReNeg()", setup="from __main__ import FiltReNeg", number=1))
    print (timeit.timeit("ListReNeg()", setup="from __main__ import ListReNeg", number=1))