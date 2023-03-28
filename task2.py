"""
Read the data from one of the task02 text files.
The data from this file contains 3 numbers on each line.  Determine how many lines of this file contains Pythagorean triples.
Pythagorean triples are numbers where all of the sides are integers, and the 3 sides form a right triangle.
The triples contained are : { 2a : 6, 2b: 4, 2c: 11}
"""

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

print(f'{listA}\n{listB}\n{listC}')

for i in enumerate(listA):
    if listA[int(i[1])]==''or listA[int(i[((i[0])+1)])]=='': 
    #or listA[(i[0]+1)[1]]=='' or listA[(i[0]+2)[1]]=='':
        print('ur agy')
    else:
        a=int(i[1])+1
        b=int(i[1])+2
        c=int(i[1])
        if int(listA[c])**2+int(listA[a])**2==int(listA[b])**2 or int(listA[a])**2+int(listA[b])**2==int(listA[c])**2 or int(listA[c])**2+int(listA[b])**2==int(listA[a])**2:
            print('borgir')

