def hasSingleCycle(array):
    # Write your code here.
    numElementVisited = 0
    currentIdx = 0
    while currentIdx < len(array):
        if numElementVisited > 0 and currentIdx == 0:
            return False
        numElementVisited += 1
        currentIdx = getNext(currentIdx, array)
    return currentIdx == 0

def getNext(currentIdx, array):
    jump = array[currentIdx]
    nextIdx = (currentIdx + jump) % len(array)
    return nextIdx if nextIdx >= 0 else nextIdx + len(array)

array = [2, 3, 1, -4, -4, 2]
a = hasSingleCycle(array)
print(a)
