# Kadane's algorithm first try:

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = nums[0]

        for num in nums:
            currSum = max(currSum, 0) + num
            maxSum = max(maxSum, currSum)
        
        return maxSum