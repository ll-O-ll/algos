def findClosestValueInBst(tree, target, closest = float('inf')):
    # Write your code here.
	#use recursion
	
    if tree is None:
        return closest
    if abs(target - closest) > abs (target - tree.value):
        closest = tree.value #initializes if root exists and looks at currentNode vs. nextNode
    if target < tree.value:
        return findClosestValueInBst(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBst(tree.right, target, closest)
    else:   
        return closest


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self



if __name__ == "__main__":
    test = BST(100).insert(5).insert(15).insert(5).insert(2).insert(1).insert(22) \
    .insert(1).insert(1).insert(3).insert(1).insert(1).insert(502).insert(55000) \
    .insert(204).insert(205).insert(207).insert(206).insert(208).insert(203) \
    .insert(-51).insert(-403).insert(1001).insert(57).insert(60).insert(4500)
    print(findClosestValueInBst(test,1002))
