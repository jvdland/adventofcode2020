import os
def read_instructions():
    instructions = []
    fn = os.path.join(os.path.dirname(__file__), 'puzzle1.input')
    #fn = os.path.join(os.path.dirname(__file__), 'sample1.input')
    with open(fn) as f:
        for l in f:
            instructions.append(l.strip())
    return instructions    
    

        

instructions = read_instructions()
jump = 0
acc = 0
index = 0
visited = []
while index not in visited:
    print("index: " + str(index))
    visited.append(index)
    i = instructions[index]
    pair = i.split()
    command = pair[0]
    digit = int(pair[1])

    if command == 'nop':
        index += 1
    
    if command=='acc':
        acc += digit
        index += 1
    
    if command=='jmp':
        index += digit
    if index in visited:
        print("instruction : "+i)

print(acc)
