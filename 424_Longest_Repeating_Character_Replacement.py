# My solution: 120 ms, likely due to max(data.values())

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        maxLength = 0
        data = {}

        for R in range(len(s)):
            if s[R] not in data:
                data[s[R]] = 1
            else:
                data[s[R]] += 1
            
            while 1 + R - L - max(data.values()) > k:
                data[s[L]] -= 1
                L += 1

            maxLength = max(maxLength, 1 + R - L)

        return maxLength
    
# Neetcode solution: 60 ms, more efficient (99%)
    
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        
        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

        return (r - l + 1)
