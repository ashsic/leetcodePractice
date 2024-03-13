# simple two pointer modified palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""

        for character in s:
            if character.isalpha():
                newS += character.lower()
            elif character.isdigit():
                newS += character
        
        L = 0
        R = len(newS) - 1

        while L <= R:
            if newS[L] != newS[R]:
                return False
            L += 1
            R -= 1
        
        return True