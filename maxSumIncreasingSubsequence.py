def maxSumIncreasingSubsequence(array):
    sums = [0] * len(array)
    sequences = [None] * len(array)
    maxSum = float("-inf")
    if len(array) == 0:
        return [0,[]]
     
    
    for i in range(len(array)):
        sums[i] += array[i]
        for j in range(0, i + 1):
            if array[i] > array[j]:
                if sums[i] < array[i] + sums[j]:
                    sums[i] = array[i] + sums[j]
                    sequences[i] = j
    maxIndx = sums.index(max(sums))
    subSequence = [array[maxIndx]]
    while sequences[maxIndx] is not None:
        maxIndx = sequences[maxIndx]
        subSequence.append(array[maxIndx])
    return [max(sums), sorted(subSequence)]
        
if __name__ == '__main__':
    print(maxSumIncreasingSubsequence([10, 15, 4, 5, 11, 14, 31, 25, 31, 23, 25, 31, 50]))
        
    

 