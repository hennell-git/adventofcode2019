
inputfile = open('input.txt').read()

rawdata = list(map(int, inputfile.split(",")))

def add(pos1, pos2, posout, srclist):
    if posout < len(srclist):
        srclist[posout] = srclist[pos1] + srclist[pos2]

def multilply(pos1, pos2, posout, srclist):
    if posout < len(srclist):
        srclist[posout] = srclist[pos1] * srclist[pos2]

def run(data):
    index = 0
    opcode = data[index]
    while opcode != 99:
        if opcode == 1:
            add(data[index+1], data[index+2], data[index+3], data), 
        if opcode == 2:
            multilply(data[index+1], data[index+2], data[index+3], data)
        index += 4
        opcode = data[index]
    return data[0]

for noun in range(0,99):
    for verb in range(0,99):
        testdata = rawdata[:]
        testdata[1] = noun
        testdata[2] = verb
        result = run(testdata)
        if result == 19690720:
            print (f"noun {noun}")
            print (f"verb: {verb}")
            break
        