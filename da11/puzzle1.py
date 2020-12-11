import os

def read_input():
    floor_plan = []
    fn = os.path.join(os.path.dirname(__file__), 'puzzle1.input')
    #fn = os.path.join(os.path.dirname(__file__), 'sample1.input')
    with open(fn) as f:
        for l in f:
            floor_plan.append(list(l.strip()))
            
    return floor_plan

def give_adjacent_seats(row_index, seat_index, floor_plan):
    res = []
    #row above
    if row_index > 0:
        if seat_index > 0:
            res.append(floor_plan[row_index-1][seat_index-1])
        res.append(floor_plan[row_index-1][seat_index])
        if seat_index < len(floor_plan[row_index])-1:
            res.append(floor_plan[row_index-1][seat_index+1])
    
    #row itself
    if seat_index > 0:
        res.append(floor_plan[row_index][seat_index-1])
    if seat_index < len(floor_plan[row_index])-1:
        res.append(floor_plan[row_index][seat_index+1])

    #row below
    if row_index < len(floor_plan) -1:
        if seat_index > 0:
            res.append(floor_plan[row_index+1][seat_index-1])
        res.append(floor_plan[row_index+1][seat_index])
        if seat_index < len(floor_plan[row_index])-1:
            res.append(floor_plan[row_index+1][seat_index+1])

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
            elif seat == '#' and neighbors.count('#') > 3:
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