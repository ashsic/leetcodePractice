class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        data = {}
        for letter in s:
            if letter not in data:
                data[letter] = 1
            else:
                data[letter] += 1

        for letter in t:
            if letter not in data or data[letter] == 0:
                return False
            data[letter] -= 1
        
        for key in data:
            if data[key] > 0:
                return False

        return True