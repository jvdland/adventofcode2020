import os
def get_passes():
    fn = os.path.join(os.path.dirname(__file__), 'puzzle1.input')
    with open(fn) as f:
        boarding_passes = f.readlines()
    return boarding_passes


def find(letters, base):
    res = base
    i = 1
    for l in letters : 
        if l =='F' or l == 'L' :
            res = res - (base // (2 ** i))
        i+=1
    return res - 1

highest = 0
for boarding_pass in get_passes():
    row_nr = find(boarding_pass.strip()[:7], 128)
    seat_nr = find(boarding_pass.strip()[7:], 8)
    id=(row_nr*8)+seat_nr
    if id > highest:
        highest = id

print(highest)
    
