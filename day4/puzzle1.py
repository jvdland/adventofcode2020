import os

def read_passports() :
    fn = os.path.join(os.path.dirname(__file__), 'puzzle1.input')
    passports = []
    pasport=[]
    with open(fn,'r') as rf:
        for line in rf:
            if line == "\n":
                passports.append(pasport)
                pasport = []
            else:
                line_keys = []
                tuples = line.strip().split(" ")
                for tuple in tuples: 
                    line_keys.append(tuple.split(":")[0])
                pasport = pasport + line_keys
    #fuck this, I need to read the last passport because it's not follwed by a \n.......
    passports.append(pasport)
    return passports

needs_to_have_keys = set(['ecl', 'iyr', 'hcl', 'byr', 'pid', 'eyr', 'hgt'])
def is_valid_passport(passport):
    if needs_to_have_keys.issubset(set(passport)) :
        return True
    return False    

passports = read_passports()
valid = 0
for passport in passports:
    if is_valid_passport(passport) :
        valid += 1  
