f = open('input.txt', 'r')
signal = f.read()[:-1]
f.close()
for loc in range(len(signal) - 3):
    chars = signal[loc: loc + 14]
    if len(set(chars)) == 14:
        break
print('first marker after character:', loc + 14)
