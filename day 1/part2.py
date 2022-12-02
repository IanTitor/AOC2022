f = open('input.txt', 'r')
cals = f.read()
f.close()
cals = cals.replace('\n\n', '], [').replace('\n', ', ')
cals = eval('[[' + cals + ']]')
greatest = 0
for elf in range(len(cals)):
    cals[elf] = sum(cals[elf])
cals = sorted(cals)[-3:]
topsum = sum(cals)
print('sum of top 3 is:', topsum)
