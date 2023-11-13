# Needed to watch half a Neetcode video for this one
# Need to study BSTs and recursion more

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        root = TreeNode(preorder[0])
        m = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:1+m], inorder[:m])
        root.right = self.buildTree(preorder[1+m:], inorder[m+1:])
        return root