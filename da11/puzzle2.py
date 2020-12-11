import os

def read_input():
    floor_plan = []
    fn = os.path.join(os.path.dirname(__file__), 'puzzle1.input')
    #fn = os.path.join(os.path.dirname(__file__), 'sample1.input')
    with open(fn) as f:
        for l in f:
            floor_plan.append(list(l.strip()))
            
    return floor_plan


def find_seat_in_line_of_sight(row_index, seat_index,x_step, y_step, floor_plan) :
    x = seat_index
    y = row_index

    if y + y_step < 0 or y + y_step == len(floor_plan):
        return []
    
    res = []
    seat = "."
    while seat == ".":
        #out of bounds Y
        if y + y_step < 0 or y + y_step == len(floor_plan):
            break
        #out of bounds X
        if x + x_step < 0 or x + x_step == len(floor_plan[y]):
            break
        x = x + x_step
        y = y + y_step
        seat = floor_plan[y][x]
    if seat != '.':
        res.append(seat)
    return res

def give_adjacent_seats(row_index, seat_index, floor_plan):
    res = []
    #left above diagonal
    res.extend(find_seat_in_line_of_sight(row_index, seat_index,-1, -1, floor_plan))
    #above
    res.extend(find_seat_in_line_of_sight(row_index, seat_index,0, -1, floor_plan))
    #right above diagonal
    res.extend(find_seat_in_line_of_sight(row_index, seat_index,1, -1, floor_plan))
    #right
    res.extend(find_seat_in_line_of_sight(row_index, seat_index,1, 0, floor_plan))
    #right below diagonal
    res.extend(find_seat_in_line_of_sight(row_index, seat_index,1, 1, floor_plan))
    #below
    res.extend(find_seat_in_line_of_sight(row_index, seat_index,0, 1, floor_plan))
    #lef below diagonal
    res.extend(find_seat_in_line_of_sight(row_index, seat_index,-1, 1, floor_plan))
    #left
    res.extend(find_seat_in_line_of_sight(row_index, seat_index,-1, 0, floor_plan))
    return res

def print_floor_plan(floor_plan):
    print("============================================================")
    for i, row in enumerate(floor_plan):
        print(str(i) + " : " +str(row))

def occupy_seats(floor_plan, prev) :
    new_floor_plan = []
    for i, row in enumerate(floor_plan):
        new_floor_plan.append([])
        for j, seat in enumerate(row):
            neighbors = give_adjacent_seats(i, j, floor_plan)
            letter = "."
            if seat == 'L' and not '#' in neighbors:
                letter="#"
            elif seat =='L':
                letter = "L"
            elif seat == '#' and neighbors.count('#') > 4:
                letter="L"
            elif seat =='#':
                letter = '#'
            #print("("+str(i) + "," + str(j) + ") is "+ seat +" , with neighbors : " + str(neighbors) + " -> " + letter)
            new_floor_plan[i].append(letter)

    current = sum(row.count('#') for row in new_floor_plan)
    #print_floor_plan(new_floor_plan)
    if current == prev:
        return current
    return occupy_seats(new_floor_plan, current)

floor_plan = read_input()
seats_occupied = occupy_seats(floor_plan, 0)

print(seats_occupied)