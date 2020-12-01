def multiplyList(myList) :
     
    # Multiply elements one by one
    result = 1
    for x in myList:
         result = result * x 
    return result 

#
# O(n2) version of finding a pair of 3 elements from a list that matches a sum
#

def findThreeElementsEqualsSumInArray(data, sum) :
    data.sort()
    remainder_list = list(data)
    for x in data :
        remainder_list.pop(0)
        remainder = sum - x
        subset = findPairEqualsSumInArray(remainder_list, remainder)
        if len(subset) :
            subset.append(x)
            return subset


#
# O(n) solution for find pair for sum in list
#
def findPairEqualsSumInArray(data, sum) :
    data.sort()
    l = 0
    r = len(data) - 1
    while l < r :
        if data[l] + data[r] == sum:
            print("found sum " + str(sum) + " for elements: left[" + str(data[l]) + "], right[" + str(data[r]) + "]")
            return [data[l], data[r]]
        elif data[l] + data[r] < sum:
            l+=1
        else:
            r-=1
    print("NOT FOUND")
    return []

filename ="day1/puzzle1.input"
# read filelines into array
with open(filename) as f:
    data = f.readlines()
# remove whitespace, convert to int
data = [int(x.strip()) for x in data] 
#print(multiplyList(findPairEqualsSumInArray(content, 2020)))
subset = findThreeElementsEqualsSumInArray(data, 2020)
print(subset)
print("Answer : " + str(multiplyList(subset)))