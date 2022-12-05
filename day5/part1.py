f = open('input.txt', 'r')
info = f.read()[:-1]
f.close()
info = info.split('\n')
numOfStacks = int((len(info[0]) + 1) / 4)
cargo = [[] for x in range(numOfStacks)]
row = 0
while info[row][0] != ' ':
    for col in range(numOfStacks):
        if info[row][col * 4 + 1] != ' ':
            cargo[col] = [info[row][col * 4 + 1]] + cargo[col]
    row += 1
operations = info[row + 2:]
for operation in operations:
    amount, origin, destination = eval(operation.replace('move ', '').replace(' from', ', ').replace(' to', ', '))
    for x in range(amount):
        cargo[destination - 1].append(cargo[origin - 1].pop(-1))
topCrates = ''
for col in cargo:
    topCrates += col[-1]
print('top crates are:', topCrates)
