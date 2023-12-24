# Leetcode daily problem. Couldn't figure it out so got a hint that gave it away.

class Solution:
    def minOperations(self, s: str) -> int:
        count0 = 0
        count1 = 0

        for x in range(len(s)):
            if x % 2 == 0:
                if s[x] == '1':
                    count0 += 1
                else:
                    count1 += 1
            else:
                if s[x] == '1':
                    count1 += 1
                else:
                    count0 += 1
        
        return min(count0, count1)