# Multiple algorithms below:

# Insertion Sort:
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            j = i - 1
            while j >= 0:
                if nums[j+1] < nums[j]:
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
                j -= 1
        return nums
                
# [2, 3, 5, 1]
# [2, 3, 1, 5]
# [2, 1, 3, 5]

# Merge Sort:

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(mergedArr, leftArr, rightArr):
            i, l, r = 0, 0, 0
            while l < len(leftArr) and r < len(rightArr):
                if leftArr[l] <= rightArr[r]:
                    mergedArr[i] = leftArr[l]
                    l+=1
                else:
                    mergedArr[i] = rightArr[r]
                    r+=1
                i+=1

            mergedArr = mergedArr[:i] + leftArr[l:] if leftArr[l:] else rightArr[r:]

        def mergeSort(arr):
            if len(arr) <= 1:
                return
            
            mid = len(arr) // 2
            arrL = arr[:mid]
            arrR = arr[mid:]

            mergeSort(arrL)
            mergeSort(arrR)
            merge(arr, arrL, arrR)
        
        mergeSort(nums)
        return nums
    
# Quick sort coming soon...