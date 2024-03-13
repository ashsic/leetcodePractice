# bit manip, got this one myself after learning some more
# about how to interact with binary nums in python

class Solution:
    def reverseBits(self, n: int) -> int:
        data = 0

        for x in range(32):
            if n & 1 == 1:
                data += 2 ** (31 - x)
            n = n >> 1

        return data