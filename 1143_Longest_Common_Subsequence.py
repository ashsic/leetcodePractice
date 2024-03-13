# My memo solution - took a long time and a look at my notes. Not optimal

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        grid = [[0] * len(text2) for _ in range(len(text1))]

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    if i >= 1 and j >= 1:
                        grid[i][j] = grid[i-1][j-1]
                    grid[i][j] += 1
                    continue
                if i - 1 >= 0:
                    grid[i][j] = grid[i - 1][j]
                if j - 1 >= 0:
                    grid[i][j] = max(grid[i][j - 1], grid[i][j])

        return grid[-1][-1]