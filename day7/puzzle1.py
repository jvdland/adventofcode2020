import os, re
def read_rules():
    fn = os.path.join(os.path.dirname(__file__), 'puzzle1.input')
    #fn = os.path.join(os.path.dirname(__file__), 'sample1.input')
    rules = {}
    with open(fn) as f:
        for line in f:
            pair = line.split("contain")
            parent = pair[0].replace("bags", "").strip()
            children = [re.sub(" \d+", "", w) for w in pair[1].split(",")]
            children = [w.replace(".", "").replace("bags", "").replace("bag","").strip() for w in children]
            rules[parent] = children

    return rules

def find_parents_for_key(key, allready_found, rules):
    res = []
    for parent, children in rules.items():
        if key in children and parent not in allready_found:
            res.append(parent)
            allready_found.append(parent)
            res.extend(find_parents_for_key(parent, allready_found, rules))
    return res

rules = read_rules()
res = find_parents_for_key('shiny gold', [], rules)
print(len(res))