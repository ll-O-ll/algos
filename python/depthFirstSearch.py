class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
		# basically know what depth first search is... 
        #what took your time: returning... don't return if there's no useful if-statement...
        #need useful return ____ and simple call to function() as in this caseb
        #don't let yourSelf be affected next tim
        array.append(self.name)
        for i in range(len(self.children)):
            self.children[i].depthFirstSearch(array) #call child with current array
        return array


if __name__ == '__main__':
    test1 = Node("A")
    test1.addChild("B").addChild("C")
    test1.children[0].addChild("D")
    print(test1.depthFirstSearch([]))
    
    