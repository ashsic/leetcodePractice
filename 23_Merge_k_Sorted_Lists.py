# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(left, right):
            l, r = 0, 0
            dummy = ListNode()
            curr = dummy
            while left and right:
                if left.val <= right.val:
                    curr.next = left
                    left = left.next
                else:
                    curr.next = right
                    right = right.next
                curr = curr.next
            
            curr.next = left if left else right
            return dummy.next

        if not lists:
            return None

        while len(lists) > 1:
            newLists = []
            for i in range(0, len(lists), 2):
                lList1 = lists[i]
                lList2 = lists[i + 1] if (i + 1) < len(lists) else None
                newLists.append(merge(lList1, lList2))

            lists = newLists

        return lists[0]