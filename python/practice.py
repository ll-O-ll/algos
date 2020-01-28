def selectionSort(array):
    for currIdx in range(len(array) -1):
        minIdx = currIdx
        for i in range(currIdx+1, len(array)):
            if array[i] <= array[minIdx]:
                minIdx = i
        array[currIdx], array[minIdx] = array[minIdx], array[currIdx]
    return array