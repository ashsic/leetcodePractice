# Leetcode hard never seen before, dijkstra's sol'n in less than 20 mins

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        time = grid[0][0]
        minHeap = [(time, 0, 0)]
        neighbours = [[1,0], [0,1], [-1,0], [0,-1]]

        cache = set()
        
        while minHeap:
            t, i, j = heapq.heappop(minHeap)
            cache.add(t)
            if t > time:
                time = t
            if i == n - 1 and j == n - 1:
                return time
            
            for di, dj in neighbours:
                i2 = i + di
                j2 = j + dj
                if (i2 >= n or j2 >= n or
                    i2 < 0 or j2 < 0 or
                    grid[i2][j2] in cache):
                    continue
                heapq.heappush(minHeap, (grid[i2][j2], i2, j2))
            