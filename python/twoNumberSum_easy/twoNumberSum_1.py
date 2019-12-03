def twoNumberSum(array, targetSum):
    answer = []
	array.sort(reverse=False)
	for i in range(len(array)):
		for j in range(i+1,len(array)):
			if (array[i]+array[j]) == targetSum:
				answer.append(array[i])
				answer.append(array[j])
	return answer
