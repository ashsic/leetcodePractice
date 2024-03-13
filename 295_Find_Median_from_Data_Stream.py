class MedianFinder:

    def __init__(self):
        self.small = []
        self.big = []


    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        if (self.small and self.big and (self.small[0] * -1 > self.big[0])):
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.big, val)
        
        # balance heaps
        if (len(self.small) > len(self.big) + 1):
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.big, val)
        if (len(self.big) > len(self.small) + 1):
            val = heapq.heappop(self.big) * -1
            heapq.heappush(self.small, val)

    def findMedian(self) -> float:

        if len(self.small) > len(self.big):
            return self.small[0] * -1
        elif len(self.big) > len(self.small):
            return self.big[0]

        return (-1 * self.small[0] + self.big[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()