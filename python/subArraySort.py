def subarraySort(array):
   # plan of action: assume there exist a subarray which is unordered
		# within the unordered subarray we need two values... the min and max vals.. 
	  	# the min num must be at the position closest to the start of the subarray
		# the max num must be at the postiion closest to the end of the the subarray
		#bisA
        #AlH
        #missed simple case: when entire array is sorted return [-1,-1]         
		
	minNumInSubArray = float("inf") #-> seemed counterintuitive but because we want the min have "-inf" will always yield "-inf"
	maxNumInSubArray = float("-inf")

    for i in range(len(array)):
        num = array[i]
        if IsOutOfOrder(i, num, array):
            minNumInSubArray = min(num, minNumInSubArray)
            maxNumInSubArray = max(num, maxNumInSubArray)
    if minNumInSubArray == float("inf"):
        return [-1,-1]
    leftIdxSubArray = 0
    rightIdxSubArray = len(array) - 1
    while array[leftIdxSubArray] <= minNumInSubArray:
        leftIdxSubArray += 1
    while array[rightIdxSubArray] >= maxNumInSubArray:
        rightIdxSubArray -= 1
    return [leftIdxSubArray, rightIdxSubArray]

def IsOutOfOrder(index, num, array):
    if index == 0:
        return num > array[index+1]
    if index == len(array) - 1:
        return num < array[index-1]
    return num > array[index+1] or num < array[index-1]  # DeMorgan's Law !{ arr[i-1] <= arr[i] and arr[i] <= array[i+1] } 
                                                 #                               Not (A and B) = (not A) or (not B) gets rid of equal signs