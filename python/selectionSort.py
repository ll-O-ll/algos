def selectionSort(array):
    #select the min element of each suffix... the suffix state going from array -> subarray -> singleton
    # s_index stores the index which determines the size of the suffix
    #PLAY WITH INDEX SELECT
    for s_index in range(len(array)-1):
        min_index = s_index
        for i in range(s_index+1,len(array)):
            # find selection = min(subarray)
            if array[i] < array[min_index]:
                min_index = i
        array[s_index], array[min_index] = array[min_index], array[s_index]
    return array
if __name__ == '__main__':
    print(selectionSort([5, -2, 2, -8, 3, -10, -6, -1, 2, -2, 9, 1, 1]))
    