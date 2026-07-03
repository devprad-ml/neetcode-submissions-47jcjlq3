# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        stk = []
        ans = []
        v = None


        curr = root

        while stk or curr:
            while curr:
                stk.append(curr)
                curr = curr.left
            
            peek = stk[-1]

            if not peek.right or peek.right == v:
                curr = stk.pop()
                ans.append(curr.val)
                v = peek
                curr = None
            else:
                curr = peek.right
        
        return ans