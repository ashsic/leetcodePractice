# Daily problem, true single pass that beat 100%

class Solution:
    def maxScore(self, s: str) -> int:
        score = 0
        maxScore = -math.inf
        numOnes, numZeroes = 0, 0

        for i in range(len(s)):
            if s[i] == '0' and i < len(s) - 1:
                score += 1
                numZeroes += 1
            elif s[i] == '1':
                score -= 1
                numOnes += 1
            if score > maxScore:
                maxScore = score
                numOnes = 0
                finalZeroes = numZeroes

        return finalZeroes + numOnes