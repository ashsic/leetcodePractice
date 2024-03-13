class Solution:
    def pivotInteger(self, n: int) -> int:
        num1 = (n * (n + 1)) // 2
        num2 = 0

        for i in range(n, -1, -1):
            num2 += i
            if num2 == num1:
                return i
            num1 -= i

        return -1
