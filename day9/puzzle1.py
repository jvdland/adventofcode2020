import os

def read_instructions():
    numbers = []
    fn = os.path.join(os.path.dirname(__file__), 'puzzle1.input')
    #fn = os.path.join(os.path.dirname(__file__), 'sample1.input')
    with open(fn) as f:
        for l in f:
            numbers.append(int(l.strip()))
            
    return numbers

def is_sum_of_parts(parts, number):
    parts.sort()
    found = False
    i = 0
    j = len(parts) -1
    while(i < j):
        sum = parts[i] + parts[j]
        if sum == number:
            found = True
            break
        if sum > number :
            j -= 1
        if sum < number :
            i +=1

    return found

numbers = read_instructions()
preamble_size = 25
i = preamble_size

while i < len(numbers):
    preamble = numbers[i-preamble_size:i]
    print("number : " + str(numbers[i]) + ", preamble : " +str(preamble))
    if not is_sum_of_parts(preamble, numbers[i]):
        print("found the bastard! : " + str(numbers[i]))
        break
    i+=1
