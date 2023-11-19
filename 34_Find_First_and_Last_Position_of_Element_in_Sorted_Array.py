# another binary search problem, a twist on first bad version 

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                submid = mid
                while nums[l] != target:
                    subl = (l + submid) // 2
                    if nums[subl] < target:
                        l = subl + 1
                    else:
                        submid = subl - 1

                submid = mid
                while nums[r] != target:
                    subr = (submid + r) // 2
                    if nums[subr] > target:
                        r = subr - 1
                    else:
                        submid = subr + 1

                return l, r

        return -1, -1