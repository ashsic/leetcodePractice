# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val < val:
            return self.searchBST(root.right, val)
        elif root.val > val:
            return self.searchBST(root.left, val)
        return root
    
# Recursive above, iterative below. 
# curr and root should be swapped but I already wrote it...

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        while root:
            if root.val > val:
                if root.left:
                    root = root.left
                else:
                    root.left = TreeNode(val)
                    break
            elif root.val < val:
                if root.right:
                    root = root.right
                else:
                    root.right = TreeNode(val)
                    break
            
        return curr if curr else TreeNode(val)