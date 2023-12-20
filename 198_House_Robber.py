# My memoization solution:

class Solution:
    def rob(self, nums: List[int]) -> int:
        data = {}

        for i, num in enumerate(nums):
            if i <= 1:
                data[i] = num if i == 0 else max(num, data[i - 1])
                continue
            data[i] = max(data[i - 1], data[i - 2] + num)
        
        return data[len(nums) - 1]
    
# classic DP approach - really confused me compared to memoization
    
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        
        data = [nums[0], max(nums[0], nums[1])]

        for num in range(2, len(nums)):
            temp = data[1]
            data[1] = max(data[1], data[0] + nums[num])
            data[0] = temp
        
        return data[1]
