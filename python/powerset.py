def powerset(array, idx = None):
    if idx is None:
        idx = len(array) - 1 
    if idx < 0:
        return [[]]
    ele = array[idx]
    subsets = powerset(array, idx - 1)
    for i in range(len(subsets)):
        subsets.append(subsets[i] + [ele])
    return subsets

def powerset2(array):
    subsets = [[]]
    for ele in array:
        newsubSets = []
        for subset in subsets:
            subset = subset + [ele]
            newsubSets.append(subset)
        subsets = subsets + newsubSets
    return subsets	

def powerset3(array):
    subsets = [[]]
    for ele in array:
        for i in range(len(subsets)):
            subsets.append(subsets[i] + [ele])
    return subsets	
    
if __name__ == '__main__':
    print(powerset([1,2]))
    