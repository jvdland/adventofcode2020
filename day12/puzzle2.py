import os
from itertools import cycle, islice

def read_instructions():
    res = []
    fn = os.path.join(os.path.dirname(__file__), 'puzzle1.input')
    #fn = os.path.join(os.path.dirname(__file__), 'sample1.input')
    with open(fn) as f:
        for l in f:
            res.append(l.strip())
    return res

def move(way_point, distance, position) : 
    position[0] += int(distance) * way_point[0]
    position[1] += int(distance) * way_point[1]
    return position

def move_waypoint(direction, distance, way_point):
    movement = int(distance)
    if direction == 'N' :
        way_point[1] += movement
    elif direction =='S' :
        way_point[1] -= movement
    elif direction == 'E' :
        way_point[0] += movement
    else :
        way_point[0] -= movement
    return way_point

def rotate_waypoint(letter, number, way_point):
    steps = int(int(number) / 90)
    i = 0
    while i < steps : 
        tmp = [0,0]
        if letter == 'R' : 
            tmp [0] = way_point[1]
            tmp [1] = way_point[0] * -1
        else : 
            tmp [0] = way_point[1] * -1
            tmp [1] = way_point[0]
        way_point = tmp
        i += 1
    return way_point


def process_instruction(way_point, current_pos, instruction) :
    letter = instruction[0]
    number = instruction[1:]
    if letter =='F' : 
        current_pos = move(way_point, number, current_pos)
    elif not(letter == 'L' or letter =='R') :
        way_point = move_waypoint(letter, number, way_point)
    else :
        way_point = rotate_waypoint(letter, number, way_point) 
    return way_point, current_pos

way_point = [10, 1]
current_pos = [0,0]

instructions = read_instructions()
for instruction in instructions:
    print("waypoint : " + str(way_point) + " , pos : " + str(current_pos) )
    way_point, current_pos = process_instruction(way_point, current_pos, instruction)

print(current_pos)
