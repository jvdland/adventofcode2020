import os
from itertools import cycle, islice

directions_r = ['N', 'E', 'S', 'W']
directions_l = ['N', 'W', 'S', 'E']

def read_instructions():
    res = []
    fn = os.path.join(os.path.dirname(__file__), 'puzzle1.input')
    #fn = os.path.join(os.path.dirname(__file__), 'sample1.input')
    with open(fn) as f:
        for l in f:
            res.append(l.strip())
    return res

def move(direction, distance, position) : 
    movement = int(distance)
    if direction == 'N' :
        position[1] += movement
    elif direction =='S' :
        position[1] -= movement
    elif direction == 'E' :
        position[0] += movement
    else :
        position[0] -= movement
    return position

def change_direction(rotation, degrees, current_direction):
    if rotation == 'R':
        directions = directions_r
    else : 
        directions = directions_l
    start = directions.index(current_direction)
    steps = int(int(degrees) / 90)
    i = 0
    loop = islice(cycle(directions), start+1, None)
    while i < steps : 
        current_direction = next(loop)
        i += 1
    return current_direction


def process_instruction(current_direction, current_pos, instruction) :
    letter = instruction[0]
    number = instruction[1:]
    if letter =='F' : 
        current_pos = move(current_direction, number, current_pos)
    elif not(letter == 'L' or letter =='R') :
        current_pos = move(letter, number, current_pos)
    else :
        current_direction = change_direction(letter, number, current_direction) 
    return current_direction, current_pos

current_direction = "E"
current_pos = [0,0]

instructions = read_instructions()
for instruction in instructions:
    #print(str(current_pos) + " : dir " + str(current_direction))
    current_direction, current_pos = process_instruction(current_direction, current_pos, instruction)

print(current_pos)
