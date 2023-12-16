# My first solution

import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for x in points:
            x.insert(0, -(x[0] ** 2 + x[1] ** 2))
        
        heapq.heapify(points)
        while len(points) > k:
            heapq.heappop(points)
        
        return [x[1:] for x in points]
    
# Refined solution
    
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        
        for x, y in points:
            if len(heap) == k:
                heapq.heappushpop(heap, [-(x**2 + y**2), x, y])
            else:
                heapq.heappush(heap, [-(x**2 + y**2), x, y])
        
        return [x[1:] for x in heap]
    
# Solution from other user - 630 vs 680 ms
    
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        heap = []
        
        for (x, y) in points:
            dist = -(x*x + y*y)
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))
        
        return [(x,y) for (dist,x, y) in heap]