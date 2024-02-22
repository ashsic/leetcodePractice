class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(i):
            if i == len(nums):
                return [[]]
            
            resPerms = []
            perms = helper(i+1)
            for p in perms:
                for j in range(len(nums) - i):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    resPerms.append(pCopy)
            return resPerms
        
        return helper(0)
        