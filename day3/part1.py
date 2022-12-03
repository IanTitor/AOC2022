f = open('input.txt', 'r')
contents = f.read()[:-1]
f.close()
contents = contents.split('\n')
prioritySum = 0
for c in range(len(contents)):
    half = int(len(contents[c])/2)
    sameItem = list(set(contents[c][:half]).intersection(set(contents[c][half:])))[0]
    prioritySum += (ord(sameItem) - 38) % 58
print('sum of common item priorities is:', prioritySum)
