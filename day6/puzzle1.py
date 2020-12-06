import os
def read_answers() :
    fn = os.path.join(os.path.dirname(__file__), 'puzzle1.input')
    all_answers = []
    group_answers=[]
    with open(fn,'r') as rf:
        for line in rf:
            if line == "\n":
                all_answers.append(set(group_answers))
                group_answers = []
            else:
                group_answers = group_answers + list(line.strip())
    all_answers.append(set(group_answers))
    return all_answers


answers = read_answers()
count = 0
for answer in answers : 
    count = count + len(answer)


print(answers)
print(count)