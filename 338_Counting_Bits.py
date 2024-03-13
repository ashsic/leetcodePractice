# My slow ass solution, 170 ms:

class Solution:
    def countBits(self, n: int) -> List[int]:
        data = []

        for x in range(n + 1):
            count = 0
            for _ in range(32):
                if x & 1 == 1:
                    count += 1
                x = x >> 1

            data.append(count)

        return data
    
# The "proper" way, 60 ms:
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp
    
# Both used dynamic programming, but the pattern is hard to see for the second one...