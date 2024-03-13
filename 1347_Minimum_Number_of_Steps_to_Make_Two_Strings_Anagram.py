class Solution:
    def minSteps(self, s: str, t: str) -> int:
        data = {}

        for c in s:
            if c not in data:
                data[c] = 1
            else:
                data[c] += 1

        count = 0

        for d in t:
            if d in data:
                data[d] -= 1
                if data[d] == 0:
                    del data[d]
            else:
                count += 1

        return count