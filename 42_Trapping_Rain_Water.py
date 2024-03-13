# This one really pissed me off. chased bad solutions for hours instead of
# adapting container with most water to this problem.

# My solution: 4000 ms

class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        volume = 0

        while L < R:
            if height[L + 1] >= height[L]:
                L += 1
            elif height[R - 1] >= height[R]:
                R -= 1
            else:
                i = L + 1
                localMax = height[i]
                maxIndex = i
                while i < R and height[i] < height[L]:
                    i += 1
                    if height[i] > localMax:
                        localMax = height[i]
                        maxIndex = i
                if i == R:
                    i = maxIndex

                minHeight = min(height[L], height[i])
                for x in range(L + 1, i):
                    if minHeight - height[x] > 0:
                        volume += minHeight - height[x]
                L = i
        
        return volume

# Neetcode solution: 100 ms
    
class Solution:
    def trap(self, height: List[int]) -> int:
        L = 0
        R = len(height) - 1
        volume = 0
        leftMax = height[L]
        rightMax = height[R]

        while L < R:
            if leftMax < rightMax:
                L += 1
                leftMax = max(height[L], leftMax)
                volume += leftMax - height[L]
            else:
                R -= 1
                rightMax = max(height[R], rightMax)
                volume += rightMax - height[R]
        
        return volume