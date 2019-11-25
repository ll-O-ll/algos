def searchInSortedMatrix(matrix, target):
    # Write your code here.
    # all I can think of is an O(n^2) solution...
    row = 0
    col = len(matrix[0]) - 1 #we start at the end so we can get both greater than/lesser than comparisons
    while row != len(matrix) and col >= 0:
        if matrix[row][col] > target: # lesser than comparison
            col -= 1
        elif matrix[row][col] < target: # greater than comparison
            row += 1
        else:
            return [row, col]
    return [-1,-1]

if __name__ == '__main__':
    target = 128
    matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004],
]
    print(searchInSortedMatrix(matrix, target))
    