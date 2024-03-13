# my solution - slow 700 ms

from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:   
        visit = set()
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        length = 1
        if grid[0][0] == 0:
            queue.append((0,0))
            visit.add((0,0))

        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == rows - 1 and c == cols - 1:
                    return length

                directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
                for dr, dc in directions:
                    if (min(r + dr, c + dc) < 0
                        or r + dr == rows or c + dc == cols
                        or (r + dr, c + dc) in visit
                        or grid[r + dr][c + dc] == 1):
                        continue
                    queue.append((r + dr, c + dc))
                    visit.add((r + dr, c + dc))  
            length += 1
        return -1
    
# Neetcode solution, 500ms
    
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = deque([(0, 0, 1)]) # r, c, length
        visit = set((0, 0))
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0],
                  [1, 1], [-1, -1], [1, -1], [-1, 1]]
        while q:
            r, c, length = q.popleft()
            if (min(r, c) < 0 or max(r, c) >= N or
                grid[r][c]):
                continue
            if r == N - 1 and c == N - 1:
                return length
            for dr, dc in direct:
                if (r + dr, c + dc) not in visit:
                    q.append((r + dr, c + dc, length + 1))
                    visit.add((r + dr, c + dc))
        return -1