# Hashmap time!

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        data = {}
        for num in nums:
            if num in data.keys():
                return True
            data[num] = 1
        
        return False