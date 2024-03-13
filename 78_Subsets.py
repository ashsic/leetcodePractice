# First rough solution:

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(nums, subset, x):
            if x >= len(nums):
                subsetsArr.append(subset.copy())
                return

            subset.append(nums[x])
            helper(nums, subset, x+1)
            subset.pop()
            helper(nums, subset, x+1)

        subsetsArr = []
        subset = []
        helper(nums, subset, 0)

        return subsetsArr

# Second refined solution, not needed to pass arrays, just index:

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(x):
            if x >= len(nums):
                subsetsArr.append(subset.copy())
                return
            
            subset.append(nums[x])
            dfs(x+1)
            subset.pop()
            dfs(x+1)


        subsetsArr = []
        subset = []
        dfs(0)

        return subsetsArr