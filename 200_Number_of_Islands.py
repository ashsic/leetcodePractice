# My solution with modifying the matrix:

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def matrixDFS(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == '0':
                return
            grid[r][c] = '0'

            matrixDFS(r + 1, c)
            matrixDFS(r - 1, c)
            matrixDFS(r, c + 1)
            matrixDFS(r, c - 1)       
        
        rows = len(grid) 
        cols = len(grid[0])
        count = 0
        for x in range(rows * cols):
            if grid[x // cols][x % cols] == '1':
                matrixDFS(x // cols, x % cols)
                count += 1
        
        return count