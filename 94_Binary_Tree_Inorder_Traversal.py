# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(root, data):
            if root.left:
                data = traverse(root.left, data)

            data.append(root.val)

            if root.right:
                data = traverse(root.right, data)

            return data
        
        if not root:
            return []
        
        data = traverse(root, [])
        return data
    
# Based on learning iterative inorder BST traversal for #230 via Neetcode, created this sol'n:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []
        stack = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            inorder.append(curr.val)

            curr = curr.right
        
        return inorder