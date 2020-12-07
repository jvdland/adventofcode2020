import os, re
child_with_parents = {}
def read_rules():
    #fn = os.path.join(os.path.dirname(__file__), 'sample1.input')
    fn = os.path.join(os.path.dirname(__file__), 'puzzle1.input')
    rules = []
    with open(fn) as f:
        for line in f:
            rule = line.strip().split("contain")
            left = [rule[0].replace("bags", "").strip()]
            right = rule[1].strip().split(',')
            right = [w.replace('bags', '').replace('bag', '').replace('.', '').strip() for w in right]
            right = [re.sub('\d', '', w).strip() for w in right]
            left.extend(right)
            rules.append(left)
    return rules

def add_parents(rule, child_with_parents) :
    parent = rule.pop(0)
    for child in rule :
        if not child in child_with_parents.keys():
            child_with_parents[child] = set()
        child_with_parents[child].add(parent)
    return child_with_parents

def add_grand_parents(child_with_parents):
    for child, parents in child_with_parents.items():
        for parent in parents :
            if parent in child_with_parents.keys():
                child_with_parents[child] = child_with_parents[child].union(child_with_parents[parent])
    return child_with_parents

rules = read_rules()
for rule in rules:
    child_with_parents = add_parents(rule, child_with_parents)

child_with_parents = add_grand_parents(child_with_parents)
child_with_parents = add_grand_parents(child_with_parents)
child_with_parents = add_grand_parents(child_with_parents)


print(len(child_with_parents['shiny gold']))