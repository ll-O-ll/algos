def insertionSort(array):
    #the suffix is the next element in the array which will be inserted into the subarray;
    #it is a singleton
    for suffix_index in range(1,len(array)): 
        for subarray_index in range(0,suffix_index+1):
            if array[suffix_index] <= array[subarray_index]:
                array[subarray_index],array[suffix_index] = array[suffix_index], array[subarray_index] 
    return array
if __name__ == '__main__':
    print(insertionSort([-7, 2, 3, 8, -10, 4, -6, -10, -2, -7, 10, 5, 2, 9, -9, -5, 3, 8]))
    