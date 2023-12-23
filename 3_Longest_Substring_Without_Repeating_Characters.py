# sliding window var size again. pretty easy

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        data = set()
        L = 0
        maxLength = 0
        count = 0

        for R in range(len(s)):
            while s[R] in data:
                data.remove(s[L])
                L += 1
            data.add(s[R])
            maxLength = max(maxLength, 1 + R - L)
        
        return maxLength