# loop:
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        
        while n > 2:
            if n % 2:
                return False
            n = n / 2

        return n == 2 or n == 1
  



# no loops, no recursion:
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n <= 0 or n % 2:
            return False
        return float("%.10f"%(math.log(n, 2))) == int(math.log(n, 2))
        