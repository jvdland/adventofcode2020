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

ids=[]
for boarding_pass in get_passes():
    row_nr = find(boarding_pass.strip()[:7], 128)
    seat_nr = find(boarding_pass.strip()[7:], 8)
    id=(row_nr*8)+seat_nr
    ids.append(id)
ids.sort()
prev = ids[0]
i=1
while i < len(ids):
    if ids[i] - prev != 1 :
        print("next seat is " + str(ids[i]) + " , so your seat is : "+ str(ids[i]-1))
    prev = ids[i]
    i+=1
    
