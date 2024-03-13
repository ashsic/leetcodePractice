from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        rows = len(grid)
        cols = len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        q = deque()
        oranges = set()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
                elif grid[row][col] == 1:
                    oranges.add((row, col))

        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    if (min(r + dr, c + dc) < 0 or r + dr == rows or c + dc == cols
                        or not grid[r + dr][c + dc] == 1):
                        continue
                    oranges.remove((r + dr, c + dc))
                    grid[r + dr][c + dc] = 2
                    q.append((r + dr, c + dc))
            if q:
                time += 1

        return time if not oranges else -1