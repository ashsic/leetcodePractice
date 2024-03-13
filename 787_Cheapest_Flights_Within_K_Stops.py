# BFS graph, DFS timeout, then memory exceeded, finally got this one

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        visited = [float('inf')] * n
        visited[src] = 0

        for flight in flights:
            graph[flight[0]].append((flight[1], flight[2]))

        q = deque([(src, 0)])

        while q and k >= 0:
            for x in range(len(q)):
                curr = q.popleft()    
                for dest, price in graph[curr[0]]:
                    newPrice = curr[1] + price
                    if newPrice < visited[dest]:
                        visited[dest] = newPrice
                        q.append((dest, newPrice))    
            k -= 1

        return -1 if visited[dst] == float('inf') else visited[dst]
