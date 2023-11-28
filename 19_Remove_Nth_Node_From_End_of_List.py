# Working on my recursion and linked list skills.
# Iterative 2 pass soln is trivial here, but I had to use a helper fn
# for the single pass to work.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def helper(head, n):
            if not head:
                return n
            n = helper(head.next, n)
            if n == 0:
                head.next = head.next.next
            return n - 1
        dummy = ListNode(0, head)
        helper(dummy, n)
        return dummy.next