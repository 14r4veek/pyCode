# -*- coding: utf-8 -*-
from collections import deque
import pickle
from random import randint
import os

result = randint(1,100)
history = deque([],5)
if os.path.isfile("save.data"):
    history = pickle.load(open("save.data"))

def guess(k):
    if k == result:
        print("You are right!")
        return True
    elif k > result:
        print "%s is greater than result" % k
        return False
    else:
        print "%s is less than result" % k
        return False

while True:
    line = raw_input("please input your guess number: ")

    if line.isdigit():
        k = int(line)
        history.append(k)
        if guess(k):
            break
    elif line == 'history' or line == 'h?':
        print "your input history is ",list(history)

f = open("save.data",'w')
pickle.dump(history, f)