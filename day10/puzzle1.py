import os

def read_adapters():
    res = []
    fn = os.path.join(os.path.dirname(__file__), 'puzzle1.input')
    #fn = os.path.join(os.path.dirname(__file__), 'sample1.input')
    with open(fn) as f:
        for l in f:
            res.append(int(l.strip()))
    res.sort()
    return res

adapters = read_adapters()
charger = adapters[-1] + 3
prev = 0
ones = 0
threes = 1

for adapter in adapters:
    if adapter - prev == 1:
        ones +=1
    
    if adapter - prev == 3:
        threes +=1

    if adapter - prev == 2:
        print("twoooo")
    prev = adapter
print(ones)
print(threes)
print("answer : " + str(ones * threes))