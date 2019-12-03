def threeNumberSum(array, targetSum):
    # Write your code here.
    # solution O(n^3)
    # sort... still O(n^2) time O(n) space
    array = sorted(array)
    answer = []
    for i in range(len(array)-1):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[i] + array[left] + array[right]
            if currentSum == targetSum:
                answer.append(sorted([array[i],array[left],array[right]]))
            #missed
                left += 1
                right -= 1
            elif currentSum > targetSum:
                right -= 1
            else:
                left += 1
    return sorted(answer)
if __name__ == '__main__':
    array = [12, 3, 1, 2, -6, 5, -8, 6]
    targetSum = 0
    print(threeNumberSum(array,targetSum))
    