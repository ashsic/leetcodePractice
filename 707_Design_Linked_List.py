class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
    # def __str__(self):
    #     data = []
    #     curr = self
    #     while curr:
    #         data.append(curr.val)
    #         curr = curr.next
    #     return str(data)

class MyLinkedList:

    def __init__(self, val=0, next=None):
        self.left = ListNode()
        self.right = ListNode()
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        curr = self.left
        for i in range(index+1):
            if curr.next:
                curr = curr.next
            if curr == self.right:
                return -1
        return curr.val

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val, self.left.next, self.left)
        self.left.next.prev = newNode
        self.left.next = newNode
        #print(self.left)

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val, self.right, self.right.prev)
        self.right.prev.next = newNode
        self.right.prev = newNode
        #print(self.left)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        else:
            curr = self.left
            for i in range(index+1):
                if curr:
                    curr = curr.next
                #print(i, curr.val)
            if curr == self.right:
                self.addAtTail(val)
            elif curr:
                newNode = ListNode(val, curr, curr.prev)
                curr.prev.next = newNode
                curr.prev = newNode
        #print(self.left)

    def deleteAtIndex(self, index: int) -> None:
        if self.left.next == self.right:
            return
        curr = self.left
        for i in range(index+1):
            if curr:
                curr = curr.next  
        if curr and curr != self.right:
            #print(self.left)
            curr.prev.next = curr.next
            curr.next.prev = curr.prev


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)