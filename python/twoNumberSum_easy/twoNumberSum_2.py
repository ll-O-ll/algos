def twoNumberSum(array, targetSum):
	#using dictionaries to solve the problem
		nums = {}
		for num in array:
				
			potentialMatch = targetSum - num
			if potentialMatch in nums:
				return sorted([potentialMatch, num])
			else:
				nums[num] = True

		return []	

if __name__ == "__main__":
	twoNumberSum([4, 6], 10)