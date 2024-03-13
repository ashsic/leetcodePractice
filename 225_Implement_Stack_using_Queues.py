class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyStack:

    def __init__(self):
        self.dummy = ListNode(0)
        self.stack = self.dummy

    def push(self, x: int) -> None:
        self.stack = ListNode(x, self.stack)

    def pop(self) -> int:
        node = self.stack.val
        self.stack = self.stack.next
        return node

    def top(self) -> int:
        return self.stack.val

    def empty(self) -> bool:
        if self.stack == self.dummy:
            return True
        return False

# Only used 1 queue, with good memory efficiency.


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()