
def binarySearch(array, target):
    return binarySearchHelper(array,target,0,len(array)-1)

def binarySearchHelper(array,target,left,right):
    # Write your code here.
	#derive the binary search algo without looking at/remembering it...
    #next for loop
    mid = (left + right) // 2
    if left > right: #left > right
        return -1
    if target == array[mid]:
        return mid
    if target < array[mid]:
        return binarySearchHelper(array,target, left, mid -1)
    elif target > array[mid]:
       return binarySearchHelper(array, target,mid+1,right)

if __name__ == '__main__':
    print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 3))
    