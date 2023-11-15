# Initial solution:

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(x):
            if x >= len(candidates) or sum(curr) >= target:
                return

            curr.append(candidates[x])
            if sum(curr) == target:
                combinations.append(curr.copy())
            dfs(x)
            curr.pop()
            dfs(x+1)

        combinations = []
        curr = []
        dfs(0)
        return combinations

# Revised solution (slightly faster?):

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(x, target):
            if x >= len(candidates) or target <= 0:
                return

            curr.append(candidates[x])
            target -= candidates[x]
            if target == 0:
                combinations.append(curr.copy())
            else:
                dfs(x, target)
            target += curr.pop()
            dfs(x+1, target)
        
        combinations = []
        curr = []
        dfs(0, target)
        return combinations
    
# Neetcode Solution:

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(x, total):
            if x >= len(candidates) or total > target:
                return
            if total == target:
                combinations.append(curr.copy())
                return

            curr.append(candidates[x])
            dfs(x, total + candidates[x])
            curr.pop()
            dfs(x+1, total)
        
        combinations = []
        curr = []
        dfs(0, 0)
        return combinations