# -*- coding: utf-8 -*-
import re
from random import randint
from collections import Counter

data = [randint(0, 20) for _ in range(100)]
c = dict.fromkeys(data, 0)

for x in data:
    c[x] += 1

c2 = Counter(data)

txt = open("doc.txt", "r").read()
c3 = Counter(re.split("\W+", txt))

if __name__ == "__main__":
    print(data)
    print(c)
    print(c2)
    print(c2.most_common(3))
    print(c3)
    print(c3.most_common(10))