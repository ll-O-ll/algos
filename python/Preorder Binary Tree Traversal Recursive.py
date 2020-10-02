# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #preorder root-> left-> right 
        List = []
        #Case 1: if the Binary tree is empty, return nothing
        if (root == None):
            return List
        #Here we define a function from within to save our list values 
        
        def preorder(root, List):

            if (root == None):
                return

            List.append(root.val)
            preorder(root.left, List)
            preorder(root.right, List)
        
        
        
        preorder(root, List)
        return List
    

        