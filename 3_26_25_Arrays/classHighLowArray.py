# Create a variable to hold the highest value
# Assign the value at element 0 to the highest
# Use a looop to step through the rest of the elements
# Each iteration a comparison is made to the highest variable
# If the element is greater than the highest value, that value is then assigned to the highest variable

import random

def getRandomList(start, end, length):
    randomList = []
    while length > 0:
        length -= 1
        randomList.append(random.randint(start, end))
    return randomList

def listHighest(localList):
    highest = localList[0]
    for x in localList:
        if x > highest:
            highest = x
    print(f"Highest: {highest}")

def listLowest(localList):
    lowest = localList[0]
    for x in localList:
        if x < lowest:
            lowest = x
    print(f"Lowest: {lowest}")

def main():
    numList = getRandomList(1, 100, 20)
    print(numList)
    listHighest(numList)
    listLowest(numList)

main()
