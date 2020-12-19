import os


def apply_mask(raw_value, mask):
    bit_string = list(format(raw_value, '036b'))
    for i, c in mask:
        bit_string[i] = c
    
    return int("".join(bit_string), 2)

memory = {}


fn = os.path.join(os.path.dirname(__file__), 'puzzle1.input')

mask = []
with open(fn) as f:
    for line in f:
        if "mask" in line : 
            mask = [(i, c) for i, c in enumerate(line.split('=')[1].strip()) if c != 'X']
        else :
            value = apply_mask(int(line.split("=")[1].strip()), mask)
            mem_key = line.split("=")[0].strip()
            memory[mem_key] = value

print(sum(memory.values()))
