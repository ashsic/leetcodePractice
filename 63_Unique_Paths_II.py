# DFS solution or more or less memoization changing existing array in place

class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            if r == len(grid) or c == len(grid[0]) or grid[r][c] == 1:
                return 0
            if grid[r][c] != 0:
                return grid[r][c]
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return -1
            
            grid[r][c] = dfs(r + 1, c) + dfs(r, c + 1)

            return grid[r][c]
        
        return -dfs(0, 0)
    
# True bottom up DP
    
class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        if grid[rows - 1][cols - 1] or grid[0][0]:
            return 0

        grid.append([0] * cols)
        grid[rows - 1][cols - 1] = -1

        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if grid[i][j] != 0:
                    continue
                grid[i][j] = grid[i + 1][j] if grid[i + 1][j] != 1 else 0
                if j < cols - 1:
                    grid[i][j] += grid[i][j + 1] if grid[i][j + 1] != 1 else 0
            
        return -grid[0][0] 