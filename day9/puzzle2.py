import os

def read_instructions():
    numbers = []
    fn = os.path.join(os.path.dirname(__file__), 'puzzle2.input')
    #fn = os.path.join(os.path.dirname(__file__), 'sample1.input')
    with open(fn) as f:
        for l in f:
            numbers.append(int(l.strip()))
            
    return numbers

numbers = read_instructions()

to_find = 552655238

def look_ahead(forward_numbers, to_find):
    tmp = 0
    series = []
    while tmp < to_find:
        el = forward_numbers.pop(0)
        series.append(el)
        tmp = tmp + el
    return tmp, series

for i, number in enumerate(numbers):
    tmp = numbers[i:]
    sum_of_parts, series = look_ahead(tmp, to_find)
    if sum_of_parts == to_find:
        series.sort()
        print("answer : " + str(series[0] + series[-1]))
        break