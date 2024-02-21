class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(i):
            if len(cur) == k:
                res.append(cur.copy())
                return
            if i > n:
                return
            
            cur.append(i)
            dfs(i+1)
            cur.pop()
            dfs(i+1)
        
        res = []
        cur = []

        dfs(1)

        return res
        
# more efficient soln:
    
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(i):
            if len(cur) == k:
                res.append(cur.copy())
                return
            if i > n:
                return

            for j in range(i, n+1):
                cur.append(j)
                dfs(j+1)
                cur.pop()
            

        res = []
        cur = []

        dfs(1)

        return res
        