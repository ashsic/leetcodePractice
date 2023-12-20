class Solution:
    def climbStairs(self, n: int) -> int:
        data = {0:1,1:1}

        for x in range(2,n+1):
            data[x] = data[x-1] + data[x-2]
        return data[n]
    
# True DP no memoization:

class Solution:
    def climbStairs(self, n: int) -> int:
        data = [1,2]

        for x in range(3, n+1):
            temp = data[1]
            data[1] = data[1] + data[0]
            data[0] = temp
        
        return data[-1] if n != 1 else 1

# DP solution with array:
    
class Solution:
    def climbStairs(self, n: int) -> int:
        data = [0,1,2,3]

        for x in range(4, n+1):
            data.append(data[-1] + data[-2])
        
        return data[n]
    
# recursive solution (timeout):

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        return self.climbStairs(n-1) + self.climbStairs(n-2)