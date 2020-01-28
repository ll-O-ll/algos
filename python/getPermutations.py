def getPermHelper(array,perm,perms):
    if len(array) == 0 and len(perm) > 0:
            perms.append(perm)
    else:
        for i in range(len(array)):
            newArr = array[:i] + array[i+1:]
            newPerm = perm + [array[i]]
            getPermHelper(newArr,newPerm,perms)
def getPermutations(array):
    # Write your code here.
    perm = []
    perms = []
    getPermHelper(array, perm, perms)
    return perms
if __name__ == '__main__':
    print(getPermutations([1,2,3]))
    