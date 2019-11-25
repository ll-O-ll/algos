def exchangeAndPartition(arr, left, right): 
    # design thought process:
    #           QuickSort says that the basic problem for sorting the list is having the following:
                       # item at position i-1   <   item at a position i  < item at position i+1
    # the way we achieve this desired state is by setting item at position i to be the pivot. 
    # the pivot can be any item in the list... to simplify things we let it be either the first, last or median index.
    # below the pivot is the last item in the list.
    # after the list transitions through a couple states we want we get closer to the desired state.
    # to get closer to the desired state, after every execution the function which will cause the state transitionning we ensure that:
    # 1. all elements to the left of the pivot will be smaller than the pivot
    # 2. all element to the right of the pivot will be greater than the pivot
    # 3. the pivot will be in the correct position in the final sorted array
    # whenever conditions 2. does not hold we know that this element
    # does there since it is smaller than pivot: we therefore swap it with the left(most) element. 
    # then we basically achieve the state where condition 1. holds.
    # after the function executed we recurse over partitions of the array. 
    # the array is split into two partitions at the position 
    # where we last swapped in the pivot. 
    # recursion will follow a tree struction where leaves would hold arrays with either  0 or 1 element
    # lastly we return the desired state of the array
    # NOTE: A HIGH LEVEL IDEA: if we take the indices of the original array and make another array 
    # with its elements being the indices of the original array, we obtain a sorted array in essence 
    itemFromLeft = left        
    pivot = arr[right]    
    for itemFromRight in range(left, right): 
        if arr[itemFromRight] < pivot: 
            arr[itemFromLeft], arr[itemFromRight] = arr[itemFromRight], arr[itemFromLeft] 
            itemFromLeft += 1
    arr[itemFromLeft], arr[right] = arr[right], arr[itemFromLeft] # one less line with pointer technology
    return itemFromLeft 

def quickSortHelper(arr, left, right): 
    if left < right: 
        p_index = exchangeAndPartition(arr,left,right) 
        quickSortHelper(arr, left, p_index-1) 
        quickSortHelper(arr, p_index+1, right) 
    return arr

def quickSort(array):
    left = 0
    right = len(array) - 1
    quickSortHelper(array, left, right)
    return array


if __name__ == '__main__': 
    arr = [2,6,5,0,8,7,1,3] 
    quickSort(arr)
    n = len(arr)
    print("Sorted array is:") 
    for i in range(n): 
        print ("%d" %arr[i]),