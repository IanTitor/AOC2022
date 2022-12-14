f = open('input.txt', 'r')
contents = f.read()[:-1]
f.close()
contents = contents.split('\n')
prioritySum = 0
for content in contents:
    half = int(len(content)/2)
    sameItem = list(set(content[:half]).intersection(set(content[half:])))[0]
    prioritySum += (ord(sameItem) - 38) % 58
print('sum of common item priorities is:', prioritySum)
