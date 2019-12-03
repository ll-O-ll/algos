def productSum(array, product = 1):
    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSum(element,product+1)
        else:
            sum += element
    return sum * product  
if __name__ == '__main__':
    test = [1, 2, [3], 4, 5]  
    print(productSum(test))
    