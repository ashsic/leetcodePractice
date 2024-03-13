class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1: return -1 if trust else 1
        
        trusted = [0] * (n + 1)

        for j in range(len(trust)):
            trusted[trust[j][0]] -= 1
            trusted[trust[j][1]] += 1
        
        for i in range(1, len(trusted)):
            if trusted[i] == n - 1:
                return i
            
        return -1
