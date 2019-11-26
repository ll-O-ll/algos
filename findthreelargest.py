def findFourLargestNumbers(array):
    # Write your code here.
    answer = []
    answer.append(array[0])
    answer.append(array[1])
    answer.append(array[2])
    answer.append(array[3])
    for i in range(4,len(array)):
        if  array[i] >= min(answer):
            answer.pop(answer.index(min(answer)))
            answer.append(array[i])
    return sorted(answer)

if __name__ == '__main__':
    print(findFourLargestNumbers([7, 55, 11, 324, 111, 212, 3, 43, 9]))
    