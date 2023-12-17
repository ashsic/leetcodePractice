# hashmap two sum soln

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}
        
        for i, num in enumerate(nums):
            if target - num in data.keys():
                return [i, data[target - num]]
            data[num] = i