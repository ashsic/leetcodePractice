# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def find(root, k):
            if root.left:
                k = find(root.left, k)
            else:
                k -= 1
            
            if k == 0:
                data[0] = root.val
            
            if root.right:
                k = find(root.right, k)
            else:
                k -= 1
            
            return k
        
        if not root:
            return
        data = [0]
        find(root, k)
        return data[0]

# Neetcode solution below: (iterative)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            k-=1
            if k == 0:
                return curr.val
            curr = curr.right