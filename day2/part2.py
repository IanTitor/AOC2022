f = open('input.txt', 'r')
rounds = f.read()[:-1]
f.close()
rounds = rounds.replace('A', '1').replace('B', '2').replace('C', '3').replace('X', '1').replace('Y', '2').replace('Z', '3').replace(' ', ', ').replace('\n', '], [')
rounds = eval('[[' + rounds + ']]')
score = 0
for r in rounds:
    score += r[1] * 3 - 3
    if r[1] == 1:
        score += (r[0] - 2) % 3 + 1
    if r[1] == 2:
        score += r[0]
    if r[1] == 3:
        score += r[0] % 3 + 1
print('your score is:', score)
