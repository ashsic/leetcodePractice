class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(x):
            p = parent[x]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p
        
        def union(x,y):
            p1, p2 = find(x), find(y)
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
            elif rank[p1] < rank[p2]:
                parent[p1] = p2
            else:
                parent[p1] = p2
                rank[p1] += 1
            return True
        
        parent = {}
        rank = {}
        for i in range(1,len(edges)+1):
            parent[i] = i
            rank[i] = 0

        last = []

        for x, y in edges:
            if not union(x,y):
                last = [x,y]
        
        return last
