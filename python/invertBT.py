def invertBinaryTree(tree):
    # Write your code here.
    if tree is None:
        return 
    if tree.left is not None or tree.right is not None:
        swapChildren(tree)
        invertBinaryTree(tree.left)
        invertBinaryTree(tree.right)
    return tree
        
        
def swapChildren(parentNode):
    parentNode.left, parentNode.right = parentNode.right, parentNode.left
    
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __eq__(self, other):
        return isinstance(other, type(self)) and self.__dict__ == other.__dict__

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self

    def invertedInsert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
        self.invertedInsert(values, i + 1)
        return self
if __name__ == '__main__':
    
    test4 = BinaryTree(1).insert([2, 3, 4])
    invertedTest4 = BinaryTree(1).invertedInsert([2, 3, 4])
    if invertedTest4 == invertBinaryTree(test4):
        print("pass")
    