import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        data = []
        
        for x in range(1, len(heights)):
            if heights[x] > heights[x-1]:
                diff = heights[x] - heights[x-1]
                heapq.heappush(data, -(diff))
                if (bricks >= diff):
                    pass
                elif ladders:
                    ladders -= 1
                    if data:
                        bricks -= heapq.heappop(data)
                else:
                    return x - 1
                
                bricks -= diff
                
        return len(heights) - 1
        