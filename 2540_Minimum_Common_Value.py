class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        l1 = len(nums1)
        l2 = len(nums2)

        while i < l1 and j < l2:
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                return nums1[i]
        
        return -1
