import os
def read_instructions():
    instructions = []
    fn = os.path.join(os.path.dirname(__file__), 'puzzle2.input')
    #fn = os.path.join(os.path.dirname(__file__), 'sample1.input')
    with open(fn) as f:
        for l in f:
            instructions.append(l.strip())
    return instructions    

def run(instructions):
    acc = 0
    index = 0
    visited = []
    last = len(instructions)
    runs = True
    while index < last and runs:
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
            runs = False
    return acc, visited, runs

def flip_instruction(command) :
    if 'jmp' in command:
        return command.replace('jmp', 'nop')
    elif 'nop' in command:
        return command.replace('nop', 'jmp')
    return command

def backtrack(instructions, visited, depth):
    #flip visited on index last - depth
    i = len(visited) -1 - depth
    instructions[visited[i]] = flip_instruction(instructions[visited[i]])
    return instructions

instructions = read_instructions()
depth = -1
#first run
acc, org_visited, runs = run(instructions)
while not runs:
    acc, dont_care_visited, runs = run(instructions)
    depth += 1
    instructions = backtrack(instructions, org_visited, depth)

print(acc)



