class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}

        for i in range(1, 1+n):
            adj[i] = []
        
        for s, d, t in times:
            adj[s].append((d,t))
        
        minHeap = [(0,k)]
        shortest = {}
        time = 0

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            shortest[n1] = w1
            if w1 > time:
                time = w1

            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, (w1+w2, n2))

            if len(shortest) == n:
                return time
        
        return -1
