def getNthFib2(n, lookup = [0]):
    lookup = [0]*n
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    lookup[0] = 0
    lookup[1] = 1

    for i in range(2,n):
        lookup[i] = lookup[i-1] + lookup[i-2]
    return lookup[n-1]

#O(n) solution
if __name__ == "__main__":
    print(getNthFib2(1))