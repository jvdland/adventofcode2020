import os
fn = os.path.join(os.path.dirname(__file__), 'puzzle2.input')

def validPassword(tuple):
    policy = tuple.split(":")[0].strip()
    password = tuple.split(":")[1].strip()
    letter = policy.split(" ")[1]
    present_at_position = int(policy.split(" ")[0].split("-")[0])
    absent_at_position = int(policy.split(" ")[0].split("-")[1])
    #XOR, it needs to be in either position, but not in both
    if (password[present_at_position-1] == letter) ^ (password[absent_at_position-1] == letter):
        return True
    return False

nr_valid = 0
with open(fn) as f:
    tuples = f.readlines()
    for t in tuples:
        if validPassword(t):
            nr_valid += 1



print("Answer: "+ str(nr_valid))