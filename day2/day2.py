import os
def isSafe(levels):
    if len(levels) < 2: return True

    isNonDecreasing = True
    isNonIncreasing = True

    for i in range(len(levels) -1):
        if levels[i] < levels[i+1]:
            isNonIncreasing = False
        elif levels[i] > levels[i+1]:
            isNonDecreasing = False
    
    if not(isNonDecreasing or isNonIncreasing):
        return False
    
    # check differences
    for i in range(len(levels)-1):
        diff = abs(levels[i] - levels[i+1])
        if diff < 1 or diff > 3:
            return False
    return True

def isSafeWith1Removed(levels):
    if isSafe(levels): return True

    for i in range(len(levels)):
        newLevels = levels[:i] + levels[i+1:]
        if isSafe(newLevels):
            return True

    return False

if __name__ == "__main__":
    filename = os.path.join(os.path.dirname(__file__), "levels.txt")
    with open(filename, 'r') as file:
        levels =[]
        for line in file:
            # convert each line to a list of integers
            line = list(map(int, line.strip().split()))
            levels.append(line)
    
    # count safe reports
    count = 0
    for level in levels:
        if isSafeWith1Removed(level):
            count += 1
    
    print(count)
