class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        postfix = [0] * len(nums)
        total = 0
        for i in range(len(nums) - 1, -1, -1):
            postfix[i] = total
            total += nums[i]
            
        prefix = []
        total = 0
        for i, n in enumerate(nums):
            prefix.append(total)
            total += n
            if postfix[i] == prefix[i]:
                return i

        return -1