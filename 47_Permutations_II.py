# lazy solution:

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def helper(i):
            if i == len(nums):
                return [[]]

            resPerms = []
            perms = helper(i+1)

            for p in perms:
                for j in range(len(nums) - i):
                    pCopy = p.copy()
                    pCopy.insert(j, nums[i])
                    if pCopy in resPerms:
                        continue
                    resPerms.append(pCopy)
            
            return resPerms
        
        return helper(0)

# My optimized solution, using more classic dfs/backtracking/subset algorithm plus dict as counter:

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        data = defaultdict(int)
        for n in nums:
            data[n] += 1

        resultPerms = []
        perms = []

        def helper(i):
            if i == len(nums):
                resultPerms.append(perms.copy())
                return 

            for d in data:
                if data[d] >= 1:
                    data[d] -= 1
                    perms.append(d)
                    helper(i+1)
                    perms.pop()
                    data[d] += 1

        helper(0)

        return resultPerms
        