# 9 attempts and a hint later...

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        data = {}
        prefixSum = 0
        for i, n in enumerate(nums):
            prefixSum += n

            if prefixSum == k:
                count += 1
            if prefixSum - k in data:
                count += data[prefixSum - k]
            
            if prefixSum in data:
                data[prefixSum] += 1
            else:
                data[prefixSum] = 1
        
        return count