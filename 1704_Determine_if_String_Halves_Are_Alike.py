class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = 'aeiou'
        l = 0
        r = len(s) - 1
        count = 0

        while l < r:
            if s[l].lower() in vowels:
                count += 1
            if s[r].lower() in vowels:
                count -= 1
            l += 1
            r -= 1
        
        return count == 0