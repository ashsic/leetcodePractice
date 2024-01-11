# Daily question, BST DFS w/ helper

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(curr, curr_Max, curr_Min, max_Diff):
            curr_Max = max(curr_Max, curr.val)
            curr_Min = min(curr_Min, curr.val)

            max_Diff = max(max_Diff, abs(curr_Max - curr_Min))

            if curr.left:
                max_Diff = max(max_Diff, dfs(curr.left, curr_Max, curr_Min, max_Diff))
            if curr.right:
                max_Diff = max(max_Diff, dfs(curr.right, curr_Max, curr_Min, max_Diff))
            
            return max_Diff

        return dfs(root, root.val, root.val, 0) 