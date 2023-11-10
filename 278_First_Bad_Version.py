# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n

        while l <= r:
            mid = (l + r) // 2

            checkBad = isBadVersion(mid)

            if checkBad:
                r = mid - 1
                last = mid
            else:
                l = mid + 1
        
        return last