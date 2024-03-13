# Kadane/sliding window. Took me a while but got it first try

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        maxDistance = 1
        curDistance = 1
        L, R = 0, 1
        isLess = True
        isGreater = True

        while R < len(arr):
            if arr[L] < arr[R] and isLess:
                curDistance += 1
                L += 1
                isLess = False
                isGreater = True
            elif arr[L] > arr[R] and isGreater:
                curDistance += 1
                L += 1
                isLess = True
                isGreater = False
            else:
                if arr[L] != arr[R]:
                    R -= 1
                L = R
                curDistance = 1
                isLess = True
                isGreater = True
                
            R += 1
            maxDistance = max(maxDistance, curDistance)

        return maxDistance