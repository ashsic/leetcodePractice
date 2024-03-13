"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# My first dirty brute force solution

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        adjList = {}
        q = deque([node])
        while q:
            node = q.popleft()
            if node.val not in adjList:
                adjList[node.val] = [Node(node.val)]
            for i in range(len(node.neighbors)):
                if node.neighbors[i].val not in adjList:
                    q.append(node.neighbors[i])
                    adjList[node.neighbors[i].val] = [Node(node.neighbors[i].val)]
                adjList[node.val].append(node.neighbors[i].val)

        for key, value in adjList.items():
            for i in value[1:]:
                value[0].neighbors.append(adjList[i][0])

        return adjList[1][0]

# My updated clean solution after thinking about it for a while

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        adjList = {}

        def dfs(curr):
            if curr.val in adjList:
                return
            adjList[curr.val] = Node(curr.val)

            for i in curr.neighbors:
                dfs(i)
                adjList[curr.val].neighbors.append(adjList[i.val])

        dfs(node)

        return adjList[1]
