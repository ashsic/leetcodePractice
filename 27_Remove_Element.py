class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[r] == val:
                r-=1
            elif nums[l] != val:
                l+=1
            else:
                nums[l], nums[r] = nums[r], nums[l]

        return r+1