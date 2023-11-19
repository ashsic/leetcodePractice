class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] < target:
                if nums[r] >= nums[mid]: 
                    if nums[r] >= target:
                        l = mid + 1
                    else:
                        r = mid - 1
                else:
                    l = mid + 1

            elif nums[mid] > target:
                if nums[l] <= nums[mid]:
                    if nums[l] <= target:
                        r = mid - 1
                    else:
                        l = mid + 1
                else:
                    r = mid - 1

            else:
                return mid

        return -1


# 1,2,3,4,5,6,7,8
# 2,3,4,5,6,7,8,1
# 3,4,5,6,7,8,1,2
# 4,5,6,7,8,1,2,3
# 5,6,7,8,1,2,3,4
# 6,7,8,1,2,3,4,5
# 7,8,1,2,3,4,5,6
# 8,1,2,3,4,5,6,7