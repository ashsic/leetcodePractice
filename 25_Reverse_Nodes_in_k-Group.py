# This one took me a full hour. Hard difficulty. Going to refine solution
# but including first solution with hand tracing for posterity:

# Soln 1:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = dummy
        prev = dummy

        while curr:

            for x in range(k):
                if curr:
                    curr = curr.next

            if not curr:
                break
            
            temp = curr.next
            curr = prev.next
            before = prev
            for x in range(k):
                
                nxt = curr.next
                curr.next = None
                
                if x == 0:
                    curr.next = temp
                else:
                    curr.next = before

                before = curr
                curr = nxt

            curr = prev.next
            prev.next = before
            prev = curr

        return dummy.next

# d 1 2 3 4 5 
#   c b t   
#     p nc
# 1>3
# 2>1
# d>2
# d 2 1 3 4 5
#       c   t
#       p   n
#         b c
# 3>5, 4>3, 1>4
# d 2 1 4 3 5
#           c

# d 1 2 3 4 5 
# p b c n t

# Soln 2, eliminated a variable and a few expressions:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while head:
            for x in range(k-1):
                if head:
                    head = head.next
            if not head:
                break
            
            temp = head.next
            head = prev.next
            before = prev
            for x in range(k):
                nxt = head.next
                
                if x == 0:
                    head.next = temp
                else:
                    head.next = before

                before = head
                head = nxt

            head = prev.next
            prev.next = before
            prev = head
            head = head.next

        return dummy.next
