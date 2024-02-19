# My Segment tree solution. Can also be solved faster with Fenwick tree.

class TreeNode:
    def __init__(self, sum, L, R):
        self.sum = sum
        self.left = None
        self.right = None
        self.L = L
        self.R = R
    
    @staticmethod
    def buildTree(nums, L, R):
        if L == R:
            return TreeNode(nums[L], L, R)

        M = (L + R) // 2
        root = TreeNode(0, L, R)
        root.left = TreeNode.buildTree(nums, L, M)
        root.right = TreeNode.buildTree(nums, M+1, R)
        root.sum = root.left.sum + root.right.sum
        return root
    
    def update(self, index, val):
        if self.L == self.R:
            self.sum = val
            return
        
        M = (self.L + self.R) // 2
        if index > M:
            self.right.update(index, val)
        else:
            self.left.update(index, val)
        self.sum = self.left.sum + self.right.sum
    
    def sumRange(self, l, r):
        if (self.L == l and r == self.R) or self.L == self.R:
            return self.sum
            
        M = (self.L + self.R) // 2
        if l > M:
            return self.right.sumRange(l, r)
        elif r <= M:
            return self.left.sumRange(l, r)
        else:
            return self.left.sumRange(l, M) + self.right.sumRange(M+1, r)


class NumArray:

    def __init__(self, nums: List[int]):
        self.tree = TreeNode.buildTree(nums, 0, len(nums) - 1)
        

    def update(self, index: int, val: int) -> None:
        self.tree.update(index, val)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.tree.sumRange(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)