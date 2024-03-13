# Same as previous solution, increment L and R by 1

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 2

        for R in range(2, len(nums)):
            if nums[L] <= nums[L - 2]:
                temp = nums[L]
                nums[L] = nums[R]
                nums[R] = temp
            if nums[L] > nums[L - 2]:
                L += 1
        
        return L