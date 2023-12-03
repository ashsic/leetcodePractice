# easy one today, spent 2 hours on median of two sorted lists before giving up.
# doing this easy one to keep streak alive...

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        data = set()
        for num in nums:
            if num in data:
                return num
            else:
                data.add(num)
