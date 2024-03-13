# easy one today, spent 2 hours on median of two sorted lists before giving up.
# doing this easy one to keep streak alive...

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        data = set()
        for num in nums:
            if num in data:
                return num
            else:
                data.add(num)

# fast/slow pointer solution
                
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            if slow2 == slow:
                return slow2
            slow2 = nums[slow2]
            slow = nums[slow]