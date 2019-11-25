def reverseLinkedList(head):
    currentNode = head
    BackNode = None
    while currentNode is not None:
        followingNode = currentNode.next
        currentNode.next = BackNode
        BackNode = currentNode
        currentNode = followingNode
    return BackNode
    


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes
if __name__ == '__main__':
    test = LinkedList(0)
    print(reverseLinkedList(test).getNodesInArray())
    
        
