
inputfile = open('testinput.txt').read()

data = list(map(int, inputfile.split(",")))

def add(pos1, pos2, posout):
    data[posout] = data[pos1] + data[pos2]

def multilply(pos1, pos2, posout):
    data[posout] = data[pos1] * data[pos2]

index = 0
opcode = data[index]
while opcode != 99:
    if opcode == 1:
        add(data[index+1], data[index+2], data[index+3])
    if opcode == 2:
        multilply(data[index+1], data[index+2], data[index+3])
    index += 4
    opcode = data[index]
else:
    print ("done")
    print (data)