import os
fn = os.path.join(os.path.dirname(__file__), 'puzzle1.input')

def validPassword(tuple):
    policy = tuple.split(":")[0].strip()
    password = tuple.split(":")[1].strip()
    letter = policy.split(" ")[1]
    lower_limit = int(policy.split(" ")[0].split("-")[0])
    upper_limit = int(policy.split(" ")[0].split("-")[1])
    count = password.count(letter)
    if lower_limit <= count <= upper_limit:
        print("Found valid password : "+ password + " for policy : "+policy)
        return True
    return False

# read filelines into array
with open(fn) as f:
    tuples = f.readlines()

nr_valid = 0
for t in tuples:
    if validPassword(t):
        nr_valid += 1

print("Answer: "+ str(nr_valid))