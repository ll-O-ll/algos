from collections import deque
# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # Write your code here.       
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0) #pops the first element - FIFO
            array.append(current.name)  
            for child in current.children:
                queue.append(child)
        return array
if __name__ == '__main__':
    test1 = Node("A")
    test1.addChild("B").addChild("C")
    test1.children[0].addChild("D")
    print(test1.breadthFirstSearch([]))
    