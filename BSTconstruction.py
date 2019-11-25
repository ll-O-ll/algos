# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None # assume there's no container i.e. left & right hold
        self.right = None # the integer values

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        if (self is None):
            self = BST(value)
        elif self.value > value:
            if self.left is not None:
                self.left = self.left.insert(value)
            else:
                self.left = BST(value)
        elif self.value <= value:
            if self.right is not None:
                self.right = self.right.insert(value)
            else:
                self.right = BST(value)
        return self

    def contains(self, value, boolean = False):
        # Write your code here.
        if (self.value == value):
            return True
        if self.left is None and self.right is None:
            return boolean
        elif (self.value > value):
            boolean = self.left.contains(value,boolean)
        elif (self.value <= value):
            boolean = self.right.contains(value, boolean)
        return boolean

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        # need parent node ##########################pause
        if (self.contains(value) == True):
            node = self.findNode(value)
            if node.left is None and node.right is None:
                node = None
            elif node.left is None and node.right is not None:
                node = node.right 
            elif node.right is None and node.left is not None:
                node = node.left
            elif node.right is not None and node.left is not Node:
                minval = node.right.findMinRSubT()
                node_min = self.findNode(minval)
                tmp = node.value
                node.value = node_min.value
                node_min.value = tmp
                node.right.remove(minval)
        return self

    def findMinRSubT(self, arr = []):
        # in-order traverses all node and returns the node associated with the minimum value 
        # in the right subtree of a BST's node (input)
        if self is not None:
            if self.left is not None:
                self.left.findMinRSubT()
            arr.append(self.value)
            if self.right is not None:
                self.right.findMinRSubT()
        return arr[0]

    def findNode(self, value):
        if (self.contains(value) == True):
            if (self.value == value):
                return self
            elif (self.value > value):
                self = self.left.findNode(value)
            elif (self.value <= value):
                self = self.right.findNode(value)
            return self
        return None

if __name__ == '__main__':
    test1 = BST(10).insert(5).insert(15).insert(5).insert(2).insert(14).insert(22)
    test1.remove(2)