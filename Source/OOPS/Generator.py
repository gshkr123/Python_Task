def readfiles(filenames):
    for f in filenames:
        for line in open(f):
            yield line

def grep(pattern, lines):
    return ( line for line in lines if pattern in line)

def printlines(lines):
    for line in lines:
        print (line)

def generator():
    for i in xrange(10):
        print (i)
        yield i

def main(pattern, filenames):
    lines = readfiles(filenames)
    lines = grep(pattern, lines)
    printlines(lines)
    print (generator())

