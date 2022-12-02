f = open('input.txt', 'r')
cals = f.read()[:-1]
f.close()
cals = cals.replace('\n\n', '], [').replace('\n', ', ')
cals = eval('[[' + cals + ']]')
greatest = 0
for elf in cals:
    elfCal = sum(elf)
    if elfCal > greatest:
        greatest = elfCal
print('greatest cal is:', greatest)
