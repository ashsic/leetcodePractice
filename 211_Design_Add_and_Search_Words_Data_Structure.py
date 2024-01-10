# My BFS Solution, took me a ridiculous amount of time

from collections import deque

class TrieNode:
    def __init__(self, height=0):
        self.children = {}
        self.word = False
        self.height = height

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode(curr.height + 1)
            curr = curr.children[c]
        curr.word = True

    def search(self, word: str) -> bool:
        q = deque()
        q.append(self.root)
        while q:   
            curr = q.popleft() 

            if curr.height == len(word):
                if curr.word:
                    return True
            elif word[curr.height] != '.':
                if word[curr.height] not in curr.children:
                    continue
                q.appendleft(curr.children[word[curr.height]])
            else:
                for key in curr.children:
                    q.append(curr.children[key])
                    
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
    
# Neetcode DFS Solution:
    
class TrieNode:
    def __init__(self):
        self.children = {}  # a : TrieNode
        self.word = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word

        return dfs(0, self.root)
