f = open('input.txt', 'r')
ranges = f.read()[:-1]
f.close()
ranges = eval('[[[' + ranges.replace(',', '], [').replace('-', ', ').replace('\n', ']], [[') + ']]]')
overlaps = 0
for rangePair in ranges:
    if rangePair[1][0] <= rangePair[0][1] <= rangePair[1][1]:
        overlaps += 1
    elif rangePair[1][0] <= rangePair[0][0] <= rangePair[1][1]:
        overlaps += 1
    elif rangePair[0][0] <= rangePair[1][0] <= rangePair[0][1]:
        overlaps += 1
    elif rangePair[0][0] <= rangePair[1][1] <= rangePair[0][1]:
        overlaps += 1
print('number of overlaps is:', overlaps)
