import os, re
def read_rules():
    fn = os.path.join(os.path.dirname(__file__), 'puzzle1.input')
    rules = {}
    with open(fn) as f:
        for line in f:
            pair = line.split("contain")
            parent = pair[0].replace("bags", "").strip()
            children = [w.replace(".", "").replace("bags", "").replace("bag","").strip() for w in pair[1].split(",")]
            rules[parent] = children

    return rules 

def count_bags_for_key(key, rules):
    total = 0
    if not 'no other' in rules[key]: 
        for c in rules[key] :
            q = re.findall('\d', c)[0]
            total += int(q) + (int(q) * count_bags_for_key(c.replace(q, "").strip(), rules))
    return total

total = count_bags_for_key('shiny gold', read_rules())
print(total)