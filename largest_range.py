def largestRange(array):
    # Write your code here.
    visitedNumbers = {}
    largest_range = []
    max_length = 0
    for number in array:
        visitedNumbers[number] = False
    for number in array:
        if visitedNumbers[number]:
            continue
        current_length = 1
        before = number - 1
        after = number + 1
        while before in visitedNumbers:
            visitedNumbers[before] = True
            current_length += 1
            before -= 1
        while after in visitedNumbers:
            visitedNumbers[after] = True
            current_length += 1
            after += 1
        if current_length > max_length:
            max_length = current_length
            largest_range = [before + 1, after - 1]
    return largest_range

        
        

if __name__ == '__main__':
    print(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))
    