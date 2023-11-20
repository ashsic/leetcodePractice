# more binary search...

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == nums[l] == nums[r] != target:
                l+=1
                r-=1

            elif nums[mid] < target:
                if nums[r] >= target or nums[r] < nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1

            elif nums[mid] > target:
                if nums[l] <= target or nums[l] > nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                return True
            
        return False
