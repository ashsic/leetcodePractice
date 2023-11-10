# Trying quickselect, failed a testcase on timeout...
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         k = len(nums) - k
#         def quickSelect(s, e):
#             pivot = nums[e]
#             j = s
#             for i in range(s, e):
#                 if nums[i] < pivot:
#                     nums[j], nums[i] = nums[i], nums[j]
#                     j+=1
#             nums[e], nums[j] = nums[j], pivot

#             if j > k:
#                 return quickSelect(s, j-1)
#             elif j < k:
#                 return quickSelect(j+1, e)
#             else:
#                 return nums[j]

#         return quickSelect(0, len(nums)-1)



# One liner using built in sort
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]