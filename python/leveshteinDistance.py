def levenshteinDistance(str1, str2):
    # Write your code here.
	minEdits = [[i for i in range(len(str1) + 1)]  for j in range(len(str2)+ 1)]
	#base case
	for i in range(1,len(str2) + 1):
		minEdits[i][0] = minEdits[i-1][0] + 1

	for i in range(1, len(str2) + 1):
		for j in range(1, len(str1) + 1):
				minEdits[i][j] = min(minEdits[i - 1][j] + 1, minEdits[i][j - 1] + 1, minEdits[i - 1][j - 1] + indicator(str2[i - 1], str1[j - 1]))
	return minEdits[-1][-1]

def indicator(char1, char2):
	if char1 == char2:
		return 0
	return 1