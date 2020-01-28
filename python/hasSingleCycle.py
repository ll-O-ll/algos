def getNxtIndex(currIdx, array):
jump = (currIdx + array[currIdx]) % len(array)
return jump if jump >= 0 else jump + len(array)

def hasSingleCycle(array):
    currIdx = 0
    numOfvisited = 0
    while numOfvisited < len(array):
        if numOfVisited > 0 and currIdx == 0:
            return False
        numOfvisited += 1
        getNxtIndex(currIdx, array) 
    return currIdx == 0
        
    
if __name__ == '__main__':
    print(hasSingleCycle([1, 1, 0, 1, 1]))
    