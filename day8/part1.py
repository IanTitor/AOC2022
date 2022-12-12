import numpy as np

f = open('input.txt', 'r')
trees = f.read()[:-1]
f.close()
trees = trees.split('\n')
for t in range(len(trees)):
    trees[t] = eval('[' + ', '.join(trees[t]) + ']')
trees = np.array(trees)
width = len(trees)

visibleTrees = np.zeros((width, width), np.int64)
for rot in range(4):
    tallestTrees = np.full(width, -1) 
    for ind, row in enumerate(trees):
        visibles = np.where(row > tallestTrees)
        tallestTrees[visibles] = row[visibles]
        visibleTrees[ind, visibles] = 1
    trees = np.rot90(trees)
    visibleTrees = np.rot90(visibleTrees)

print('number of visible trees is:', np.sum(visibleTrees))
