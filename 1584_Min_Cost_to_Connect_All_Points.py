class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {}
        minHeap = []

        minCost = set([x for x in range(len(points))])
        minCost.remove(0)
        total = 0

        for j in range(1, len(points)):  
            manDist = abs(points[0][0] - points[j][0]) + abs(points[0][1] - points[j][1])
            heapq.heappush(minHeap, (manDist, j))

        while minHeap:
            if not minCost:
                return total
            price, node = heapq.heappop(minHeap)  
            if node not in minCost:
                continue
            minCost.remove(node)
            total += price

            for j in minCost:  
                manDist = abs(points[node][0] - points[j][0]) + abs(points[node][1] - points[j][1])
                heapq.heappush(minHeap, (manDist, j))

        return total
