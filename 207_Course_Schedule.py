# quick adjacency list dfs solution

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = {}
        visit = set()

        for course in prerequisites:
            if course[0] not in adjList:
                adjList[course[0]] = []
            if course[1] not in adjList:
                adjList[course[1]] = []
            adjList[course[0]].append(course[1])

        def dfs(node):
            if node not in adjList:
                return
            if node in visit:
                return False
            visit.add(node)
            while adjList[node]:
                if dfs(adjList[node].pop()) == False:
                    return False

            visit.remove(node)
            return True

        for x in adjList:
            if dfs(x) == False:
                return False

        return True