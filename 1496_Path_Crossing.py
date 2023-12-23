# Daily question December 23, 2023

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        curr = [0,0]
        data = set()
        data.add((0,0))
        for i in path:
            if i == 'N':
                curr[1] += 1
            elif i == 'S':
                curr[1] -= 1
            elif i == 'E':
                curr[0] += 1
            elif i == 'W':
                curr[0] -= 1
            
            if (curr[0], curr[1]) in data:
                return True
            data.add((curr[0], curr[1]))
        
        return False