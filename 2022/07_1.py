import sys
class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    
    def print(self, prefix):
        print(prefix + self.name + " (file, size=" + str(self.size) + ")")

class Dir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = []
        self.dirs = []
    
    def addDir(self, dir):
        self.dirs.append(dir)
    
    def hasDir(self, name):
        for dir in self.dirs:
            if dir.name == name:
                return True
        return False
    
    def hasFile(self, fileName):
        for file in self.files:
            if file.name == fileName:
                return True
        return False

    def addFile(self, file):
        self.files.append(file)
    
    def getDir(self, name):
        for dir in self.dirs:
            if dir.name == name:
                return dir

    def getSize(self):
        sum = 0
        for d in self.dirs:
            sum += d.getSize()
        for f in self.files:
            sum += f.size
        return sum
    
    def getDirsLessThan(self, maxSize):
        lst = []
        for d in self.dirs:
            tmp = d.getDirsLessThan(maxSize)
            [lst.append(t) for t in tmp]
        for d in self.dirs:
            if d.getSize() < maxSize:
                lst.append(d)
        return lst
    
    def print(self, prefix):
        print(prefix + self.name + " (dir)")
        [d.print('  ' + prefix) for d in self.dirs]
        [f.print('  ' + prefix) for f in self.files]

lines = sys.stdin.readlines()

root = None
current = None

i = 0
while i < len(lines):
    line = lines[i].strip()
    if line[0] == '$':
        command = line[2:4]
        if command == 'cd':
            dirName = line[5:]
            if dirName == '/':
                root = Dir('/', None)
                current = root
            elif dirName == "..":
                current = current.parent
            else:
                if not current.hasDir(dirName):
                    current.addDir(Dir(dirName, current))
                current = current.getDir(dirName)
        elif command == 'ls':
            i += 1
            while i < len(lines) and lines[i][0] != '$':
                line = lines[i].strip()
                items = line.split(' ')
                if items[0] == "dir":
                    if not current.hasDir(items[1]):
                        current.addDir(Dir(items[1], current))
                else:
                    if not current.hasFile(items[1]):
                        current.addFile(File(items[1], int(items[0])))
                i += 1
            else:
                i -= 1
    i += 1

lst = root.getDirsLessThan(100000)

total = 0
for d in lst:
    total += d.getSize()

print(total)