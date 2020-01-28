def bubbleSort(array):
    #in place... no extra variables needed, element by element
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            if array[i] >= array[j]: 
                array[j],array[i] = array[i], array[j]
    return array
if __name__ == '__main__':
    print(bubbleSort([-4, 5, 10, 8, -10, -6, -4, -2, -5, 3, 5, -4, -5, -1, 1, 6, -7, -6, -7, 8]))
    