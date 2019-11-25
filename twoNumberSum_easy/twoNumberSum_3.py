def twoNumberSum(array, targetSum):
    array.sort() # array has already been orderedb
	left = 0
	right = len(array) - 1
	while left < right:
		currentSum = array[left] + array[right]
		if currentSum == target:
			return [array[left],array[right]]
		elif currentSum < targetSum:
			left += 1 # give me a bigger number 
		elif currentSum > targetSum:
			right -= 1 #give me a smaller number 
	return [] #APART FROM THAT ^ return base edge case
