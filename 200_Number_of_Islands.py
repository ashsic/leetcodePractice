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
    
# Solution without modifying (slower, more memory)
    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def matrixDFS(r, c):
            if (
                r < 0 or c < 0 
                or r == len(grid) or c == len(grid[0]) 
                or grid[r][c] == '0'
                or (r, c) in visits
                ):
                return

            visits.add((r, c))

            matrixDFS(r + 1, c)
            matrixDFS(r - 1, c)
            matrixDFS(r, c + 1)
            matrixDFS(r, c - 1)

            #visits.remove((r, c))
        
        count = 0
        visits = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1' and (row, col) not in visits:
                    matrixDFS(row, col)
                    count += 1

        return count