# Pretty easy two pointer soln. did this one yesterday

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        totalWater = 0
        while l < r:
            totalWater = max(totalWater, ( min(height[l], height[r]) * (r - l) ))
            if height[l] <= height[r]:
                l+=1
            else:
                r-=1
        
        return totalWater