# More binary search, with a bit of a twist. Also a sliding window I guess.
# This one took me close to an hour, the logic is a bit confusing towards the end.
# I saw many better solutions on Leetcode, sliding window seems better here.

class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < x:
                l = mid + 1
            elif nums[mid] > x:
                r = mid - 1
            else:
                break
     
        if nums[mid] != x:
            if l >= len(nums):
                mid = r
            elif r < 0 or abs(nums[l] - x) < abs(nums[r] - x):
                mid = l
            else:
                mid = r

        l, r = mid, min(mid+1, len(nums) - 1)

        while r - l < k:
            if l > 0 and r < len(nums):
                if abs(nums[l-1] - x) <= abs(nums[r] - x):
                    l-=1
                else:
                    r+=1
            elif l == 0:
                r+=1
            else:
                l-=1

        return nums[l:r]