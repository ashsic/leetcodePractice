# using ascii codes to set string to lowercase.

class Solution:
    def toLowerCase(self, s: str) -> str:
        s2 = ""
        for letter in s:
            if 65 <= ord(letter) <= 90:
                s2 += chr(ord(letter) + 32)
            else:
                s2 += letter
        
        return s2