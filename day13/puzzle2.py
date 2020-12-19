import os

def read_instructions():
    fn = os.path.join(os.path.dirname(__file__), 'puzzle1.input')
    #fn = os.path.join(os.path.dirname(__file__), 'sample1.input')
    with open(fn) as f:
        whocares = int(f.readline())
        busses = [x.strip() for x in f.readline().split(',')]
        busses_and_minutes = [(int(i), j) for j, i in enumerate(busses) if i != 'x']
    return busses_and_minutes

busses_and_minutes = read_instructions()

print(busses_and_minutes)

t = 0
step = 1

for bus, mins in busses_and_minutes:
    # find next departure of this bus
    while (t + mins) % bus != 0:
        t += step
    # this will happen every interval of 'bus' so we multiply the step with this interval
    step *= bus

print(t)
