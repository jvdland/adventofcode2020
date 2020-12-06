import os
def intersect(lst1, lst2) : 
    return list(set(lst1) & set(lst2)) 

def read_answers() :
    fn = os.path.join(os.path.dirname(__file__), 'puzzle2.input')
    all_answers = []
    group_answers=[]
    first = True
    with open(fn,'r') as rf:
        for line in rf:
            if line == "\n":
                all_answers.append(group_answers)
                group_answers = []
                first = True
            else:
                line_answers = list(line.strip())
                if first:
                    group_answers = line_answers
                    first = False
                else:
                    group_answers = intersect(group_answers, line_answers)
    all_answers.append(group_answers)
    return all_answers


answers = read_answers()
count = 0
for answer in answers : 
    count = count + len(answer)


print(answers)
print(count)