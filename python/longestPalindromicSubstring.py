def longestPalindromicSubstring(string):
	#O(n^2) time 
	#O(1) space
	# store max algorithm + isPalindrome
	#two cases: "ab | ba" even 
			  # "ab c ba" odd
	currentLongest =  [0, 1]
	for i in range(1, len(string)):
		even = findPalindrome(string, i - 1, i)
		odd = findPalindrome(string, i - 1, i + 1)
		longest = max(even, odd, key=lambda x: x[1] - x[0])
		currentLongest = max(longest, currentLongest,  key=lambda x: x[1] - x[0])
	return string[currentLongest[0] : currentLongest[1]]

def findPalindrome(string, left, right):
	while left >= 0 and right < len(string):
		if string[left] != string[right]:
			break
		left -= 1
		right += 1
	return [left + 1, right]
	

print(longestPalindromicSubstring("abaxyzzyxf"))