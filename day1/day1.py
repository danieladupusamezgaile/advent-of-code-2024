import os
# Maybe the lists are only off by a small amount!
# To find out, pair up the numbers and measure how far
# apart they are. Pair up the smallest number in the left
# list with the smallest number in the right list, then
# the second-smallest left number with the second-smallest
# right number, and so on.
# Within each pair, figure out how far apart the two
# numbers are; you'll need to add up all of those
# distances. For example, if you pair up a 3 from the
# left list with a 7 from the right list, the distance
# apart is 4; if you pair up a 9 with a 3, the distance
# apart is 6.

#Count how many times each number in the left list 
# appears in the right list.
# Multiply each number in the left list by its count in 
# the right list.
# Sum all these products to get the total similarity 
# score.

# read the file and return the numbers in two lists
def readListsFromFile(filename):
    leftList = []
    rightList = []

    with open(filename, 'r') as file:
        for line in file:
            # split line in left and right numbers
            left, right = map(int, line.strip().split())
            leftList.append(left)
            rightList.append(right)
    
    return leftList, rightList

# calculate total distance of both lists
def totalDistance(leftList, rightList):
    # sort both lists
    leftSorted = sorted(leftList)
    rightSorted = sorted(rightList)

    totalDistance = 0
    # loop through each pair and add up total distance
    for i in range(len(leftSorted)):
        leftNum = leftSorted[i]
        rightNum = rightSorted[i]
        distance = abs(leftNum-rightNum)
        totalDistance += distance
    
    return totalDistance

def similarityScore(leftList, rightList):
    similarityScore = 0

    for num in leftList:
        # count num of num's in right list
        count = rightList.count(num)
        # multiply num with count and add to score
        similarityScore += num * count
    
    return similarityScore


if __name__ == "__main__":
    filename = os.path.join(os.path.dirname(__file__), "lists.txt")
    leftList, rightList = readListsFromFile(filename)
    totalDistance = totalDistance(leftList, rightList)
    print(f"Total distance: {totalDistance}")
    similarityScore = similarityScore(leftList, rightList)
    print(f"Similarity score: {similarityScore}")