f = open('input.txt', 'r')
output = f.read()[:-1]
f.close()
output = output.split('\n')

class directory:
    def __init__(self, name, parent = None, layer = -1):
        self.name = name
        self.parent = parent
        self.layer = layer
        self.content = {}
        self.size = 0
    def __getitem__(self, name):
        if name == -1:
            return self.parent
        else:
            return self.content[name]
    def tree(self):
        for name in self.content:
            if type(self.content[name]) == file:
                print('\t' * self.layer, self.content[name].name, self.content[name].size)
            else:
                print('\t' * self.layer, self.content[name].name)
                self.content[name].tree()
    def updateSize(self, size):
        self.size += size
        if self.parent != None:
            self.parent.updateSize(size)
    def addDir(self, name):
        self.content[name] = directory(name, self, self.layer + 1)
    def addFile(self, name, size):
        self.content[name] = file(name, size)
        self.updateSize(size)
class file:
    def __init__(self, name, size):
        self.name = name
        self.size = size

fileSystem = directory('computer', None, -1)
fileSystem.addDir('/')
currentDir = fileSystem
sizeSum = 0
for line in output:
    line = line.split(' ')
    if line[0] == '$':
        if line[1] == 'cd':
            if line[2] == '..':
                if currentDir.size <= 100000:
                    sizeSum += currentDir.size
                currentDir = currentDir[-1]
            else:
                currentDir = currentDir[line[2]]
    elif line[0] == 'dir':
        currentDir.addDir(line[1])
    else:
        currentDir.addFile(line[1], int(line[0]))
print('total sum of the total sizes of directories with sizes of at most 100000:', sizeSum)
