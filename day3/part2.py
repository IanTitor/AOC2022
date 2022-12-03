f = open('input.txt', 'r')
contents = f.read()[:-1]
f.close()
contents = contents.split('\n')
prioritySum = 0
for c in range(0, len(contents), 3):
    sameItem = list(set(contents[c]).intersection(set(contents[c + 1])).intersection(set(contents[c + 2])))[0]
    prioritySum += (ord(sameItem) - 38) % 58
print('sum of common item priorities is:', prioritySum)
