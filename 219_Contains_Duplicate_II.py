class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        data = set()
        L = 0

        for R in range(len(nums)):
            if nums[R] in data:
                return True
            data.add(nums[R])
            if R - L >= k:
                data.remove(nums[L])
                L += 1
            
        return False