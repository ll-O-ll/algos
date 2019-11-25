def findThreeLargestNumbers(array):
    # Write your code here.
    answer = []
    answer.append(array[0])
    answer.append(array[1])
    answer.append(array[2])
    for i in range(3,len(array)):
        if  array[i] >= min(answer):
            answer.pop(answer.index(min(answer)))
            answer.append(array[i])
    return sorted(answer)

if __name__ == '__main__':
    print(findThreeLargestNumbers([7, 8, 3, 11, 43, 55]))
    