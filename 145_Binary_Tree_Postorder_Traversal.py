# Recursive soln

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(root):
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
            
            res.append(root.val)
        if root:
            dfs(root)
        return res
    
# Iterative soln
    
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [root]
        visits = [False]

        while stack:
            curr = stack.pop()
            v = visits.pop()
            if curr:
                if v:
                    res.append(curr.val)
                else:
                    stack.append(curr)
                    visits.append(True)
                    stack.append(curr.right)
                    visits.append(False)
                    stack.append(curr.left)
                    visits.append(False)
            
        return res
