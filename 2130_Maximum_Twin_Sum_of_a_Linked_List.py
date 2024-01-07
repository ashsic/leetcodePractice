# My hashmap solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        data = {}
        ctr = 0
        while head:
            data[ctr] = head.val
            head = head.next
            ctr += 1
        
        maxSum = 0
        for i in range(ctr - 1, (ctr - 1) // 2, -1):
            sum = data[i] + data[ctr - (i + 1)]
            maxSum = max(maxSum, sum)
        
        return maxSum

# Neetcode 2 ptr solution:

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        res = 0
        while slow:
            res = max(res, slow.val + prev.val)
            prev = prev.next
            slow = slow.next
        
        return res