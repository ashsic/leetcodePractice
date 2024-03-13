# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        targetSum -= root.val
        print(root.val, targetSum)
        if not root.right and not root.left and targetSum == 0:
            return True
        if self.hasPathSum(root.left, targetSum):
            return True
        if self.hasPathSum(root.right, targetSum):
            return True
        
        targetSum += root.val
        return False