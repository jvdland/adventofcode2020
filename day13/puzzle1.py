import os

def read_instructions():
    fn = os.path.join(os.path.dirname(__file__), 'puzzle1.input')
    #fn = os.path.join(os.path.dirname(__file__), 'sample1.input')
    with open(fn) as f:
        timestamp = int(f.readline())
        busses = [x.strip() for x in f.readline().split(',') if x != 'x']  
    return timestamp, busses

timestamp, busses = read_instructions()
next_departure = timestamp * 100
bus_to_take = 0
for bus in busses:
    this_bus_departs_at = (int(bus) - (timestamp % int(bus))) + timestamp
    if this_bus_departs_at < next_departure : 
        next_departure = this_bus_departs_at
        bus_to_take = bus
print("answer : " + str((next_departure-timestamp) * int(bus_to_take)))
