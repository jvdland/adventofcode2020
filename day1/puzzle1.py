#
# O(n) solution for finding a pair with a sum in a collection
#
def giveProductForPairEqualsSumInArray(data, sum) :
    data.sort()
    l = 0
    r = len(data) - 1
    while l < r :
        if data[l] + data[r] == sum:
            print("found sum " + str(sum) + " for elements: left[" + str(data[l]) + "], right[" + str(data[r]) + "]")
            return data[l] * data[r]
        elif data[l] + data[r] < sum:
            l+=1
        else:
            r-=1
    print("NOT FOUND")

filename ="day1/puzzle1.input"
# read filelines into array
with open(filename) as f:
    content = f.readlines()
# remove whitespace, convert to int
content = [int(x.strip()) for x in content] 
print("Answer : " + str(giveProductForPairEqualsSumInArray(content, 2020)))