"""
Read the data from one of the task02 text files.
The data from this file contains 3 numbers on each line.  Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are numbers where all of the sides are integers, and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}
"""
import math

filenameA = 'task02a.txt'
filenameB = 'task02b.txt'
filenameC = 'task02c.txt'

fileA = open(filenameA, 'r')
fileB = open(filenameB, 'r')
fileC = open(filenameC, 'r')

dataA = fileA.read()
dataB = fileB.read()
dataC = fileC.read()

listA = dataA.split('\n')
listB = dataB.split('\n')
listC = dataC.split('\n')

burger=[]
rightTris=[]

for i in enumerate(listA):
    burger.append(i[1])
    if i[1] == "":
        a=int(burger[0])
        b=int(burger[1])
        c=int(burger[2])
        if c**2+a**2==b**2:
            print('borgir')
            rightTris.append(b**2)
        if a**2+b**2==c**2:
            print('borgir')
            rightTris.append(c**2)
        if c**2+b**2==a**2:
            print('borgir')
            rightTris.append(a**2)
        burger.clear()
    else:
        print(burger)
    if burger==['65', '48', '45']:
        print(rightTris)
        aRights = rightTris.index((rightTris[-1]))+1
        break
rightTris.clear()
for i in enumerate(listB):
    burger.append(i[1])
    if i[1] == "":
        a=int(burger[0])
        b=int(burger[1])
        c=int(burger[2])
        if c**2+a**2==b**2:
            print('borgir')
            rightTris.append(b**2)
        if a**2+b**2==c**2:
            print('borgir')
            rightTris.append(c**2)
        if c**2+b**2==a**2:
            print('borgir')
            rightTris.append(a**2)
        burger.clear()
    else:
        print(burger)
    if burger==['28', '45', '53']:
        print(rightTris)
        bRights = rightTris.index((rightTris[-1]))+1
        break
rightTris.clear()
for i in enumerate(listC):
    burger.append(i[1])
    if i[1] == "":
        a=int(burger[0])
        b=int(burger[1])
        c=int(burger[2])
        if c**2+a**2==b**2:
            print('borgir')
            rightTris.append(b**2)
        if a**2+b**2==c**2:
            print('borgir')
            rightTris.append(c**2)
        if c**2+b**2==a**2:
            print('borgir')
            rightTris.append(a**2)
        burger.clear()
    else:
        print(burger)
    if burger==['30', '24', '19']:
        print(rightTris)
        cRights = rightTris.index((rightTris[-1]))+1
        break
print(f'task02a has {aRights} right tris\ntask02b has {bRights} right tris\ntask02c has {cRights} right tris\n')