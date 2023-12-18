# My solution with modifying matrix elements:

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def matrixDFS(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            count = 1
            count += matrixDFS(r + 1, c)
            count += matrixDFS(r - 1, c)
            count += matrixDFS(r, c + 1)
            count += matrixDFS(r, c - 1)

            return count
        
        rows = len(grid)
        cols = len(grid[0])
        maxCount = 0

        for x in range(rows * cols):
            row = x // cols
            col = x % cols
            if grid[row][col] == 1:
                maxCount = max(maxCount, matrixDFS(row, col))
            
        return maxCount