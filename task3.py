#!python
# Sum of Values

"""
The file task03.txt contains a lot of data.  Each cluster of data is the number of points for that particular group.  Each blank line indicates a separator before the next group.
Read the contents of task03.txt into your program and determine the points value of the cluster with largest sum.

For sample data task03.txt, the largest sum should be 68787
"""

filename = 'task03.txt'
file = open(filename, 'r')
data = file.read()
list = data.split('\n')

numList = []
numList2 = []
nums = []

for i in enumerate(list):
    numList.append(i[1])
    if i[1] is '':
        numList2 = numList
        numList2.remove('')
        numList2 = [int(j) for j in numList2]
        print(sum(numList2))
        nums.append(sum(numList2))
        numList.clear
        numList2.clear
    else:
        print(numList)
    if numList==['','']:
        print(nums)
        nums.sort()
        bigNum = nums[-1]
        print(bigNum)
        break

