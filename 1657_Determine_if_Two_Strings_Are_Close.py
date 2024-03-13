# Most efficient, 62 ms:

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        c1 = set(word1)
        c2 = set(word2)
        if c1 != c2:
            return False
        
        wc1 = []
        wc2 = []
        for letter in c1:
            wc1.append(word1.count(letter))
            wc2.append(word2.count(letter))

        return sorted(wc1) == sorted(wc2)
    
# One line, 130 ms:
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return len(word1) == len(word2) and sorted(Counter(word1).values()) == sorted(Counter(word2).values()) and set(word1) == set(word2)
    
# First sol'n, 300 ms:

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False

        data1 = {}
        data2 = {}
        counts = [0] * (len(word1) + 1)

        for i in range(len(word1)):
            #if word1[i] != word2[i]:
            data1[word1[i]] = data1.get(word1[i], 0) + 1 
            data2[word2[i]] = data2.get(word2[i], 0) + 1
            counts[data1[word1[i]]] += 1
            counts[data2[word2[i]]] -= 1

        print(counts)
        
        

        for x in counts:
            if x != 0:
                return False

        return True