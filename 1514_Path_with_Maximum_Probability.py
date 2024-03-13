class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for i in range(len(edges)):
            adj[edges[i][0]].append((edges[i][1], succProb[i]))
            adj[edges[i][1]].append((edges[i][0], succProb[i]))

        if not adj[end]:
            print('test')
            return 0
        
        minHeap = [(-1, start)]
        shortest = {start: -1}

        while minHeap:
            p, n = heapq.heappop(minHeap)
            shortest[n] = p
            if n == end:
                return -p
            
            for n2, p2 in adj[n]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, (p*p2, n2))
        
        return 0