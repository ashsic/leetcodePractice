class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        data = set([x for x in range(len(nums) + 1)])
        num = data.difference(set(nums))
        for i in num:
            return i
        