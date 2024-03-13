# Add two numbers, linked list, classic iterative linked list pattern
# very similar to that of merge sort "merge" part, same with K sorted lists.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while l1 and l2:
            nextVal = (curr.next.val if curr.next else 0) + l1.val + l2.val
            curr.next = ListNode(nextVal % 10)
            if nextVal // 10:
                curr.next.next = ListNode(nextVal // 10)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            nextVal = (curr.next.val if curr.next else 0) + l1.val
            curr.next = ListNode(nextVal % 10)
            if nextVal // 10:
                curr.next.next = ListNode(nextVal // 10)
            curr = curr.next
            l1 = l1.next

        while l2:
            nextVal = (curr.next.val if curr.next else 0) + l2.val
            curr.next = ListNode(nextVal % 10)
            if nextVal // 10:
                curr.next.next = ListNode(nextVal // 10)
            curr = curr.next
            l2 = l2.next

        return dummy.next