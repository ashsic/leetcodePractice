# Linked list with a stack, iterative solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        curr = head.next
        flag = True
        i = 0

        while curr:
            stack.append(curr)
            curr = curr.next
        curr = head

        while stack and i < len(stack):
            if flag:
                curr.next = stack.pop()
            else:
                curr.next = stack[i]
                i+=1
            flag = False if flag else True
            curr = curr.next
        curr.next = None
        
        return head