# My naive solution

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort()
        queue = [0] * len(people)
        #print(queue, people)

        for height, i in people:
            ind = 0
            for j in range(len(queue)):
                if queue[j]:
                    if queue[j][0] == height:
                        ind += 1
                    continue
                elif i == ind:
                    queue[j] = [height, i]
                    break
                else:
                    ind += 1

            

        return queue



#  [[6,0], [11,0], [15,0], [18,2], [20,4], [21,8]]
#
#                  [21,8]
#        [15,0]              [6,8]
#    [11,0]  [4,0]      [5,4]    [1,4]
#  [6,0] [5,0]      [3,2] [2,2]