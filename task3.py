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
list1 = data.split('\n')

numList = []
nums = []

for i in enumerate(list1):
    numList.append(i[1])
    if i[1] is '':
        print(numList)
        numList.remove(i[1])
        numList = list(map(int, numList))
        print(sum(numList))
        nums.append(sum(numList))
        if sum(numList)==35839:
            print(nums)
            nums.sort()
            bigNum = nums[-1]
            print(bigNum)
            break
        numList.clear()
    else:
        print(numList)

