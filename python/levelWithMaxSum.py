class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def levelWithMaxSum(root):
    # bread first search approach
    if root is None:
        return 0

    max_sum = float("-inf")
    queue = []
    queue.append(root)

    while len(queue) > 0:
        count = len(queue)
        sum_ = 0
        while count > 0:
            cur_node = queue.pop(0)
            sum_ += cur_node.value
            if cur_node.left is not None:
                queue.append(cur_node.left)
            if cur_node.right is not None:
                queue.append(cur_node.right)    
            count -= 1
        if sum_ > max_sum:
            max_sum = sum_ 

    return max_sum

if __name__ == "__main__":
    root = Node(12)
    leftChild = Node(23)
    leftChild.left = Node(-21)
    leftChild.right = Node(3)
    rightChild = Node(-2)
    root.left = leftChild
    root.right = rightChild
    rightChild.left = Node(-3)
    rightChild.right = Node(39)
    # Constructed Binary tree is:
    #              12
    #            /    \
    #          23     -2
    #         /  \    / \
    #        21   3 -3   39 

    print("Maximum level sum is", levelWithMaxSum(root))

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(8)
    root.right.right.left = Node(6)
    root.right.right.right = Node(7)
 
    # Constructed Binary tree is:
    #              1
    #            /   \
    #          2      3
    #        /  \      \
    #       4    5      8
    #                 /   \
    #                6     7   
    print("Maximum level sum is", levelWithMaxSum(root))
