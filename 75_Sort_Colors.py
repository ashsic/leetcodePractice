class Solution:
    def sortColors(self, nums: List[int]) -> None:
        buckets = [0, 0, 0]
        for x in nums:
            buckets[x] += 1
        i = 0
        for j in range(len(nums)):
            while buckets[i] == 0:
                i+=1
            buckets[i] -= 1
            nums[j] = i
        
        return nums
        