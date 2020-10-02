def levenshteinDistance(str1, str2):
    minEdits = [[j for j in range(len(str1) + 1)] for i in range(len(str2) + 1)]

    for i in range(len(str2) + 1):
        for j in range(len(str1)+ 1):
            if min(i,j) == 0:
                #base case: for all entries in 2D matrix where str1 or str2 = "" add one for insertion operation
                minEdits[i][j] = max(i,j)
            else:
                minEdits[i][j] = min(minEdits[i-1][j] + 1, minEdits[i][j-1] + 1, minEdits[i-1][j-1] + indicatorFunction(str1[j], str2[i]))

    return minEdits[-1][-1]


def indicatorFunction(char1, char2):
    if char1 == char2: 
        #if this conditon holds don't edit
        return 0
    return 1