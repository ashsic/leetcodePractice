class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        res = []
        cur = []

        def dfs(i):
            if i >= len(digits):
                res.append("".join(cur))
                return
            
            digit = int(digits[i])

            for l in letters[digit]:
                cur.append(l)
                dfs(i + 1)
                cur.pop()
        
        if digits:
            dfs(0)

        return res
        