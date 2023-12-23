# Sliding window sum again

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = len(nums) + 1
        total = 0
        L = 0

        for R in range(len(nums)):
            total += nums[R]
            while total >= target:
                minLength = min(minLength, 1 + R - L)
                total -= nums[L]
                L += 1
            
        return minLength if minLength <= len(nums) else 0