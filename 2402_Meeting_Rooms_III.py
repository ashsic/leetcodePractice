
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        data = [[0, 0] for x in range(n)] # val and count

        maxCount = 0
        countIndex = 0

        for s,e in meetings:

            minVal = data[0][0] + 1
            minIndex = -1
            for i,d in enumerate(data):
                if d[0] <= s:
                    d[1] += 1
                    d[0] = e
                    minIndex = -1

                    if d[1] > maxCount or (d[1] == maxCount and i <= countIndex):
                        countIndex = i
                        maxCount = d[1]

                    break
                if d[0] < minVal:
                    minVal = d[0]
                    minIndex = i
            
            if minIndex >= 0:
                data[minIndex][0] += (e - s)
                data[minIndex][1] += 1

                if data[minIndex][1] > maxCount or (data[minIndex][1] == maxCount and minIndex <= countIndex):
                    countIndex = minIndex
                    maxCount = data[minIndex][1]
             

        return countIndex
