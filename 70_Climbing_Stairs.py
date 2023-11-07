class Solution:
    def climbStairs(self, n: int) -> int:
        data = {0:1,1:1}

        for x in range(2,n+1):
            data[x] = data[x-1] + data[x-2]
        return data[n]