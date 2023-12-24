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
    
# Redoing two pointer questions right now, came to the same result more or less

class Solution:
    def maxArea(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        maxVolume = 0

        while L <= R:
            maxVolume = max((R - L) * min(height[L], height[R]), maxVolume)

            if height[L] < height[R]:
                L += 1
            else:
                R -= 1
        
        return maxVolume