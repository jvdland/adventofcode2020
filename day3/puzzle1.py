import os, math


def make_a_map():
    fn = os.path.join(os.path.dirname(__file__), 'puzzle1.input')
    map = []
    with open(fn) as f:
        rows = f.readlines()
        for row in rows :
            map.append(list(row.strip()))
    return map
    

def move_to_new_pos(current_pos, map):
    max_x_pos = len(map[0]) - 1
    if  (current_pos[0] + 3) > max_x_pos  :
        #start over
        x = current_pos[0] + 3 - max_x_pos - 1
    else:
        x = current_pos[0]+3
    return [x, current_pos[1]+1]

def is_there_a_tree_here(pos, map):
    return map[pos[1]][pos[0]] == "#"

map = make_a_map()
max_y = len(map)
print(max_y)
print(len(map[0]))
pos = [0,0]
nr_of_trees_hit = 0
while(pos[1] < max_y) :
    
    if is_there_a_tree_here(pos, map):
        nr_of_trees_hit += 1
        print(str(pos) + " YES ")
    else:
        print(pos)
    pos = move_to_new_pos(pos, map)
print(nr_of_trees_hit)

