import os, math


def make_a_map():
    fn = os.path.join(os.path.dirname(__file__), 'puzzle1.input')
    map = []
    with open(fn) as f:
        rows = f.readlines()
        for row in rows :
            map.append(list(row.strip()))
    return map
    

def move_to_new_pos(current_pos, slope, map):
    max_x_pos = len(map[0]) - 1
    if  (current_pos[0] + slope[0]) > max_x_pos  :
        #start over
        x = current_pos[0] + slope[0] - max_x_pos - 1
    else:
        x = current_pos[0]+slope[0]
    y = current_pos[1]+slope[1]
    return [x, y]

def is_there_a_tree_here(pos, map):
    return map[pos[1]][pos[0]] == "#"

def find_trees_for_slope(slope,map) :
    pos = [0,0]
    nr_of_trees_hit = 0
    while(pos[1] < len(map)) :
        if is_there_a_tree_here(pos, map):
            nr_of_trees_hit += 1
        pos = move_to_new_pos(pos, slope, map)
    return nr_of_trees_hit

map = make_a_map()
slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
trees = []
for slope in slopes:
    trees.append(find_trees_for_slope(slope,map))

print(math.prod(trees))

