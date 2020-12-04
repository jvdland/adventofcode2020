import os, re

def read_passports() :
    fn = os.path.join(os.path.dirname(__file__), 'puzzle1.input')
    passports = []
    pasport={}
    with open(fn,'r') as rf:
        for line in rf:
            if line == "\n":
                passports.append(pasport)
                pasport = {}
            else:
                tuples = line.strip().split(" ")
                for tuple in tuples:
                    pair = tuple.split(":")
                    pasport[pair[0]] = pair[1]
    #fuck this, I need to read the last passport because it's not follwed by a \n.......
    passports.append(pasport)
    return passports

needs_to_have_keys = set(['ecl', 'iyr', 'hcl', 'byr', 'pid', 'eyr', 'hgt'])
hgt_rexex = re.compile("([0-9]+)(in|cm)")
hcl_regex = re.compile("^#[a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9][a-zA-Z0-9]$")
ecl_regex = re.compile("^(amb|blu|brn|gry|grn|hzl|oth)$")
pid_regex = re.compile("^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$")

def is_valid_passport(passport):
    if not needs_to_have_keys.issubset(set(passport.keys())) :
        return False
    if not (2002 >= int(passport['byr']) >= 1920) :
        return False
    if not (2020 >= int(passport['iyr']) >= 2010) :
        return False
    if not (2030 >= int(passport['eyr']) >= 2020) :
        return False
    
    hgt_match = hgt_rexex.match(passport['hgt'])
    if(not bool(hgt_match)):
        return False
    hgt_parts = hgt_match.groups()
    if hgt_parts[1] == 'cm' and not ( 193 >= int(hgt_parts[0]) >= 150) :
        return False 
    if hgt_parts[1] == 'in' and not ( 76 >= int(hgt_parts[0]) >= 59) :
        return False
    

    if(not bool(hcl_regex.match(passport['hcl']))):
        return False
    
    if(not bool(ecl_regex.match(passport['ecl']))):
        return False
    
    if(not bool(pid_regex.match(passport['pid']))):
        return False
    print(passport['byr'])
    return True
    
    

passports = read_passports()
valid = 0
for passport in passports:
    if is_valid_passport(passport) :
        valid += 1  
print(valid)
