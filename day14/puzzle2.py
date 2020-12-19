import os, re


def apply_mask_recur(current, mask, i):
    res = []
    if not i < len(mask) : 
        res.append(current)
        return res
    j = i + 1
    c = mask[i]
    if c =='1' : 
        current[i] = '1'
        res = res + apply_mask_recur(current, mask, j)
    elif c =='X' : 
        left = current.copy()
        left[i] = '1'
        right = current.copy()
        right[i] = '0'
        res = res + apply_mask_recur(left, mask, j)
        res = res + apply_mask_recur(right, mask, j)
    else :
        res = res + apply_mask_recur(current, mask, j)
    return res



def apply_mask(org_memkey, mask):
    res = []
    bit_string = list(format(org_memkey, '036b'))
    mem_keys = apply_mask_recur(bit_string, mask, 0)
    for mem_key in mem_keys :
        res.append(int("".join(mem_key), 2))
    return res

memory = {}


fn = os.path.join(os.path.dirname(__file__), 'puzzle1.input')

mask = []
with open(fn) as f:
    for line in f:
        if "mask" in line : 
            mask = list(line.split('=')[1].strip())
        else :
            value = int(line.split("=")[1].strip())
            mem_keys = apply_mask(int(re.sub('\D', '', line.split("=")[0].strip())), mask)
            for mem_key in mem_keys:
                memory[mem_key] = value

print(sum(memory.values()))
