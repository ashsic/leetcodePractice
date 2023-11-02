class Solution: # More stack questions
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "{([":
                stack.append(i)
            elif i == ']' and (not stack or stack[-1] != '[') or\
                i == '}' and (not stack or stack[-1] != '{') or\
                i == ')' and (not stack or stack[-1] != '('):
                return False
            else:
                stack.pop()
        
        return False if stack else True