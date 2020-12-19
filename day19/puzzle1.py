import os, re

def read_rules_and_messages():
    fn = os.path.join(os.path.dirname(__file__), 'puzzle1.input')
    rules = {}
    messages = []
    reading_rules = True
    with open(fn) as f:
        while reading_rules : 
            line = f.readline().strip()
            if line == "" : 
                reading_rules = False
                break;
            key = line.split(":")[0].strip()
            rules[key] = line.split(":")[1].strip().split()
        messages = [x.strip() for x in f.readlines()]
    return rules, messages

def has_numbers(zero_rule) :
    return any(char.isdigit() for char in zero_rule)

def parse_rules_into_one(rules) :
    zero_rule = rules['0']
    while has_numbers(zero_rule) :
        new_rule = []
        for key in zero_rule:
            if key in rules:
                if '|' in rules[key]:
                    new_rule = new_rule + ['('] + rules[key] + [')']
                else :
                    new_rule = new_rule + rules[key]
            else:
                new_rule.append(key)
        zero_rule = new_rule
    #clean
    return '^' + ''.join([x.replace('"', '') for x in zero_rule]) + '$'


rules, messages = read_rules_and_messages()
pattern = re.compile(parse_rules_into_one(rules))
valid = 0
for message in messages:
    if pattern.match(message) : 
        valid +=1

print(valid)