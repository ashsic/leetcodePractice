# ANOTHER binary search. Can you tell I'm preparing for a presentation on 
# binary search? First hard that I solved with no hints, in under 20 minutes.
# Practicing with custom testcases, commented at the bottom. Explaining
# my thought process under my breath to prepare for interviews. Feel
# pretty confident about binary search, so I need to start working on some other
# algorithms soon.

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[r] < nums[mid]:
                l = mid + 1
            elif nums[r] > nums[mid]:
                r = mid
            else:
                if nums[l] > nums[mid]:
                    r = mid
                elif nums[l] < nums[mid]:
                    return nums[l]
                else:
                    if l == r:
                        return nums[l]
                    l+=1
                    r-=1
        return nums[mid]




# [1,2,3,4,5,6,7]
# [2,3,4,5,6,7,1]
# [3,4,5,6,7,1,2]
# [4,5,6,7,1,2,3]
# [5,6,7,1,2,3,4]
# [6,7,1,2,3,4,5]
# [7,1,2,3,4,5,6]

# [5,6,7,1,2,3,4]
# [0,0,0,1,2,2,4]

# [2,2,0,1,1,1,1]

# [0,0,0,1,1,1,1]

# [1,1,0,1,1,1,1]
# [1,1,1,1,0,1,1]