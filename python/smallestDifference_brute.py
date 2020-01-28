def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    # O(len(arrayOne)*len(arrayTwo)) solution
    ans = []
    ans.append(arrayOne[0])
    ans.append(arrayTwo[0])
    smallest = abs(arrayOne[0] - arrayTwo[0])
    for number1 in arrayOne:
        for number2 in arrayTwo:
            diff = abs(number1-number2)
            if diff < smallest:
                smallest = diff
                ans.pop()
                ans.pop()
                ans.append(number1)
                ans.append(number2)
    return ans
if __name__ == '__main__':
    print(smallestDifference([-1, 5, 10, 20, 3], [26, 134, 135, 15, 17]))
    
        