f = open('input.txt', 'r')
ranges = f.read()[:-1]
f.close()
ranges = eval('[[[' + ranges.replace(',', '], [').replace('-', ', ').replace('\n', ']], [[') + ']]]')
fullOverlaps = 0
for rangePair in ranges:
    if (rangePair[0][0] >= rangePair[1][0] and rangePair[0][1] <= rangePair[1][1]) or (rangePair[1][0] >= rangePair[0][0] and rangePair[1][1] <= rangePair[0][1]):
        fullOverlaps += 1
print('number of full overlaps is:', fullOverlaps)
