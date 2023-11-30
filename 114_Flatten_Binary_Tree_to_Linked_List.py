# Flatten binary tree, basically just inorder traversal appending to a list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        stack = []
        inorderArray = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                inorderArray.append(curr)
                curr = curr.left
            curr = stack.pop()
            curr = curr.right
        
        for x in range(len(inorderArray) - 1):
            inorderArray[x].right = inorderArray[x+1]
            inorderArray[x].left = None