# My initial less efficient solution:

class Median:
    def __init__(self, w):
        self.small = []
        self.big = []
        self.cap = w

    def addProject(self, prof, cap):
        if cap <= self.cap:
            heapq.heappush(self.small, [prof, cap])
        else:
            heapq.heappush(self.big, [cap, prof])
        
    def rebalance(self):
        while self.big and self.big[0][0] <= self.cap:
            cap, prof = heapq.heappop(self.big)
            heapq.heappush(self.small, [prof, cap])

    def canDoProject(self):
        if not self.small:
            return False
        return True
    
    def doProject(self):
        project = heapq.heappop(self.small)
        self.cap += project[0] * -1
        self.rebalance()
    
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        medHeap = Median(w)

        for i in range(len(profits)):
            medHeap.addProject(-1 * profits[i], capital[i])
        
        for j in range(k):
            if not medHeap.canDoProject():
                break
            medHeap.doProject()
        
        return medHeap.cap

# small change from another solution goes from 900 to 600 ms. Removed capital from minheap:
    
class Median:
    def __init__(self, w):
        self.small = []
        self.big = []
        self.cap = w

    def addProject(self, prof, cap):
        if cap <= self.cap:
            heapq.heappush(self.small, prof)
        else:
            heapq.heappush(self.big, [cap, prof])
        
    def rebalance(self):
        while self.big and self.big[0][0] <= self.cap:
            cap, prof = heapq.heappop(self.big)
            heapq.heappush(self.small, prof)

    def canDoProject(self):
        if not self.small:
            return False
        return True
    
    def doProject(self):
        self.cap -= heapq.heappop(self.small)
        self.rebalance()
    
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        medHeap = Median(w)

        for i in range(len(profits)):
            medHeap.addProject(-1 * profits[i], capital[i])
        
        for j in range(k):
            if not medHeap.canDoProject():
                break
            medHeap.doProject()
        
        return medHeap.cap
