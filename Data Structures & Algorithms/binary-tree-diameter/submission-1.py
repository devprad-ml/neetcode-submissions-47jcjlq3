# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        l = self.max_d(root.left)
        r = self.max_d(root.right)

        d = l+r

        s = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))

        return max(d, s)

    
    def max_d(self, node):
        if not node:
            return 0
        
        return 1 + max(self.max_d(node.left),self.max_d(node.right))
        


            
            
        
        
        
        