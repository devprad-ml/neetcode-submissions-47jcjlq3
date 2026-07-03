# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stk = [root]
        if not root:
            return []
        while stk:
            curr = stk.pop()
            ans.append(curr.val)

            if curr.right:
                stk.append(curr.right)
            
            if curr.left:
                stk.append(curr.left)
        
        return ans
        