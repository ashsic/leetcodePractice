class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        l, r = 1, max(piles)
        minSpeed = r
        while l <= r:
            k = (l + r) // 2
            totalHours = 0
            
            for bananas in piles:
                totalHours += math.ceil(bananas / k)
            
            if totalHours <= h:
                minSpeed = min(minSpeed, k)
                r = k - 1
            else:
                l = k + 1

        return minSpeed