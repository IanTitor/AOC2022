f = open('input.txt', 'r')
rounds = f.read()[:-1]
f.close()
rounds = rounds.replace('A', '1').replace('B', '2').replace('C', '3').replace('X', '1').replace('Y', '2').replace('Z', '3').replace(' ', ', ').replace('\n', '], [')
rounds = eval('[[' + rounds + ']]')
score = 0
for r in rounds:
    score += r[1]
    if r[1] == r[0]:
        score += 3
    if r[0] % 3 + 1 == r[1]:
        score += 6
print('your score is:', score)
