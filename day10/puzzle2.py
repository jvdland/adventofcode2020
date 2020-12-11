import os
from os import path

def read_adapters():
    res = []
    #add socket as starting point
    res.append(0)
    fn = os.path.join(os.path.dirname(__file__), 'puzzle1.input')
    #fn = os.path.join(os.path.dirname(__file__), 'sample1.input')
    with open(fn) as f:
        for l in f:
            res.append(int(l.strip()))
    res.sort()
    return res

adapters = read_adapters()
#bookkeeping to keep track of how many paths there are to a number
paths = {}
#there is 1 way to get to the first adapter
paths[adapters[0]] = 1
for cur in adapters:
    for delta in range(1, 4):
        candidate = cur + delta
        if candidate in adapters:
            #if candidate is in the adapter list, it means we have found a way to get there. 
            # We need to add all the paths that lead to where we are currently as well
            if candidate not in paths:
                paths[candidate] = paths[cur]    
            else:
                paths[candidate] += paths[cur] 

print(paths[adapters[-1]])
