# My UnionFind solution:

class UnionFind:
    def __init__(self, arr):
        self.par = {}
        self.rank = {}
        self.max = 1

        for i in arr:
            self.par[i] = i
            self.rank[i] = 1
    
    def find(self, x):
        p = self.par[x]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        
        if self.rank[px] > self.rank[py]:
            self.par[py] = px
        elif self.rank[px] < self.rank[py]:
            self.par[px] = py
        else:
            self.par[px] = py

        self.rank[py] += self.rank[px]
        self.rank[px] = self.rank[py]
        self.max = max(self.max, self.rank[px])

        return True

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        uf = UnionFind(nums)
        
        for num in nums:
            if (num - 1) in uf.par:
                uf.union(num, num-1)
            if (num + 1) in uf.par:
                uf.union(num, num+1)

        return uf.max
    
# ugly brute force solution
    
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        total = 1
        maxTotal = 1
        data = sorted(list(set(nums)))
        for i in range(1, len(data)):
            if data[i] == data[i-1] + 1:
                total += 1
            else:
                total = 1
            maxTotal = total if total > maxTotal else maxTotal

        return maxTotal