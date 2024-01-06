# First solution. both are around 175 ms

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        data = []
        for n in nums:
            product = product * n
            data.append(product)
        
        for i in range(len(nums) - 1, -1, -1):
            value = data[i - 1] if i > 0 else 1
            if (i < len(nums) - 1):
                value = value * nums[i + 1] 
                nums[i] = nums[i] * nums[i + 1]
            data[i] = value

        return data

# second solution, optimizing for fewer lines/variables

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        data = [1] * len(nums)
        for i in range(len(nums)):
            data[i] = nums[i] * (data[i - 1] if i > 0 else 1)
        
        for i in range(len(nums) - 1, -1, -1):
            data[i] = (data[i - 1] if i > 0 else 1) * (nums[i + 1] if i < len(nums) - 1 else 1)
            nums[i] *= (nums[i + 1] if i < len(nums) - 1 else 1)
            
        return data
