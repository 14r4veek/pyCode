# -*- coding: utf-8 -*-
from random import randint

student = {x: randint(50, 100) for x in "xyzabc"}
sor = sorted(zip(student.values(), student.keys()))
sor2 = sorted(student.items(), key=lambda x: x[0])
sor3 = sorted(student.items(), key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    print(student)
    print(sor)
    print(sor2)
    print(sor3)