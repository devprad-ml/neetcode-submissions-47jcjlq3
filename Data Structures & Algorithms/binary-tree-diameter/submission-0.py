# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        
        l = self.maxd(root.left)
        r = self.maxd(root.right)
        d = l+r
        s = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return max(d, s)
    
    def maxd(self, node):
        if not node:
            return 0
        return 1 + max(self.maxd(node.left), self.maxd(node.right))


            
            
        
        
        
        