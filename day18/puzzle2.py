import os, ast
def read_assignments():
    fn = os.path.join(os.path.dirname(__file__), 'puzzle1.input')
    with open(fn) as f:
        res = []
        for line in f.readlines() :
            row = '['+line.strip().replace('(', '[').replace(')', ']').replace(' ', ',').replace('*', '"*"').replace('-', '"-"').replace('+', '"+"')+']'
            list = ast.literal_eval(row)
            list = make_nested_list_for_plus(list)
            res.append(list)
        return res

def make_nested_list_for_plus(source) :
    i = 0
    while i < len(source):
        el = source[i]
        if type(el) is list: 
            source[i] = make_nested_list_for_plus(el)
        if el =='+':
            left = source[i-1]
            right = source[i+1]
            if type(right) is list:
                right = make_nested_list_for_plus(right)
            new_list = [left, '+', right]
            source[i] = new_list
            source.pop(i-1)
            source.pop(i)
            i -= 1
        i+=1
    return source

def do_math(left, operator, right):
    if operator =='+':
        return left + right
    elif operator =='-':
        return left - right
    elif operator == '*':
        return left * right
    


def do_assignment(steps) :
    left = 0
    operator = '+'
    right = None
    i=0
    while i < len(steps) :
        right = steps[i]
        if type(right) is list: 
            right = do_assignment(right)
        left = do_math(left, operator, int(right))
        if i+1 < len(steps):
            operator = steps[i+1]
            i += 2
        else :
            #last one
            i += 1
    return left

assignments = read_assignments()
sum_of_all = 0
for assignment in assignments: 
    sum_of_all += do_assignment(assignment)

print(sum_of_all)
