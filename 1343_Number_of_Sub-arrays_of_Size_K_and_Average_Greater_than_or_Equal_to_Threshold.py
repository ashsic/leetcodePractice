# Sliding window adding/subtracting elements from total

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        L = 0
        total = 0

        for R in range(len(arr)):
            total += arr[R]
            if 1 + R - L == k:
                if total / k >= threshold:
                    count += 1
                total -= arr[L]
                L += 1
        
        return count