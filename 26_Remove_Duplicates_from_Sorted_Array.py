# My python3 solution for leetcode 26. October 31st, 2023
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 1
        for y in range(1, len(nums)):
            nums[x] = nums[y]
            if nums[x] != nums[x-1]:
                x+=1
        
        return x

# Two pointer algorithm that almost looks like var window. 
# took me a while for an easy...

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 1

        for R in range(1, len(nums)):
            if nums[L] <= nums[L - 1]:
                temp = nums[L]
                nums[L] = nums[R]
                nums[R] = temp
            if nums[L] > nums[L - 1]:
                L += 1

        return L