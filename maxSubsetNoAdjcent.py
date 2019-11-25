def maxSubsetSumNoAdjacent(array):
    # Write your code here.
	dp = [0]*len(array) # stores the max sum at index i dynamically
	# base cases
	if len(array) == 0:
		return 0
	if len(array) == 1:
		return array[0]
	else:
		dp[0] = array[0] # initialize the dp
		dp[1] = max(array[0],array[1])
		for i in range(2,len(array)):
			dp[i] = max(dp[i-1], dp[i-2]+array[i])
		return dp[len(array) - 1]