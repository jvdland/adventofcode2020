import os, re

def read_rules_and_messages():
    fn = os.path.join(os.path.dirname(__file__), 'puzzle2.input')
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
                expr = rules[key]
                if key == '8':
                    #repeat rule 42
                    expr = ['(', '42', ')', '+']
                    new_rule = new_rule + ['('] + expr + [')']
                elif key == '11': 
                    # fuck this, i'm just going to repeat it!
                    expr = ['(', '42', '31',')|']
                    expr = expr + ['(', '42', '42', '31', '31',')|']
                    expr = expr + ['(', '42', '42', '42', '31', '31', '31',')|']
                    expr = expr + ['(', '42', '42', '42','42', '31', '31', '31', '31',')|']
                    expr = expr + ['(', '42', '42', '42','42', '42', '31', '31', '31', '31', '31',')|']
                    expr = expr + ['(', '42', '42', '42','42', '42', '42', '31', '31', '31', '31', '31', '31',')|']
                    expr = expr + ['(', '42', '42', '42','42', '42', '42', '42', '31', '31', '31', '31', '31', '31', '31',')|']
                    expr = expr + ['(', '42', '42', '42','42', '42', '42', '42', '42', '31', '31', '31', '31', '31', '31', '31', '31',')|']
                    expr = expr + ['(', '42', '42', '42','42', '42', '42', '42', '42', '42', '31', '31', '31', '31', '31', '31', '31', '31', '31',')|']
                    expr = expr + ['(', '42', '42', '42','42', '42', '42', '42', '42', '42', '42', '31', '31', '31', '31', '31', '31', '31', '31', '31', '31',')|']
                    expr = expr + ['(', '42', '42', '42','42', '42', '42', '42', '42', '42', '42', '42', '31', '31', '31', '31', '31', '31', '31', '31', '31', '31', '31',')|']
                    expr = expr + ['(', '42', '42', '42','42', '42', '42', '42', '42', '42', '42', '42', '42', '31', '31', '31', '31', '31', '31', '31', '31', '31', '31', '31', '31',')|']
                    expr = expr + ['(', '42', '42', '42','42', '42', '42', '42', '42', '42', '42', '42', '42', '42', '31', '31', '31', '31', '31', '31', '31', '31', '31', '31', '31', '31', '31',')|']
                    expr = expr + ['(', '42', '42', '42','42', '42', '42', '42', '42', '42', '42', '42', '42', '42', '42', '31', '31',  '31', '31', '31', '31', '31', '31', '31', '31', '31', '31', '31', '31',')']
                    new_rule = new_rule + ['('] + expr + [')']
                elif '|' in expr:
                    new_rule = new_rule + ['('] + expr + [')']
                else :
                    new_rule = new_rule + expr
            else:
                new_rule.append(key)
        zero_rule = new_rule
    #clean
    return '^' + ''.join([x.replace('"', '') for x in zero_rule]) + '$'


rules, messages = read_rules_and_messages()
regex = parse_rules_into_one(rules)
print(regex)
pattern = re.compile(regex)
valid = 0
for message in messages:
    if pattern.match(message) : 
        valid +=1

print(valid)