# My python3 solution for leetcode 26. October 31st, 2023
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 1
        for y in range(1, len(nums)):
            nums[x] = nums[y]
            if nums[x] != nums[x-1]:
                x+=1
        
        return x
