"""
Read the data from the file task02.csv
Allow the user to search for a stock symbol.
If the stock symbol is found, display the name of the company
If a multiple stocks match the symbol, say there are multiple stocks available
If there is no match, say "no match found"

Example:
Enter stock symbol: AA
There are 21 stocks with that symbol
Enter stock symbol: AAPL
Apple Inc.
Enter stock symbol: YANG
No matches
"""

filename = 'task5.csv'
file = open(filename, 'r')
data = file.read()
list1 = data.split('\n')

print(list1)

input1 = input('Enter Stock Symbol: ')
johnList = []

for i in enumerate(list1):
    specInfo = i[1].split(',')
    if input1 == specInfo[0]:
        print(specInfo[1])
        break
    for j in enumerate(list1):
        specInfo2 = j[1].split(',')
        if specInfo2[0] in input1:
            print('im agy')
            johnList.append(':)')
            a=False
        if j[0] == 'ZUMZ':
            if a==False:
                print(f'There are {johnList.index()+1} stocks with similar symbols')
            else:
                print('No matches')
