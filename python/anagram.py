def groupAnagrams(words):
    # Write your code here.
	totalAnagrams = []
	visitedAnagram = [0] * len(words) 
    for i in range(len(words)):
		if visitedAnagram[i] == 0: # use visitedAnagram to search for node.
			anagrams = []
			word1 = words[i]
			anagrams.append(word1)
			for j in range(i+1, len(words)):
				word2 = words[j]
				if isAnagram(word1, word2) and visitedAnagram[j] == 0:
					anagrams.append(word2)
					visitedAnagram[j] = 1
			totalAnagrams.append(anagrams)
	return totalAnagrams

def isAnagram(word1, word2):
	if len(word1) != len(word2):
		return False	
	letters1 = {}
	for letter in word1:
		letters1[letter] = True
		
	for letter in word2:
		if letter not in letters1:
			return False
	return True
