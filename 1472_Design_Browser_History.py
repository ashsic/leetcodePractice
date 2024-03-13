class ListNode:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage = "leetcode.com"):
        self.homepage = ListNode(homepage)
        self.curr = self.homepage

    def visit(self, url: str) -> None:
        self.curr.next = ListNode(url, None, self.curr)
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.curr.prev:
                self.curr = self.curr.prev
            else:
                break
        return self.curr.val

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.curr.next:
                self.curr = self.curr.next
            else:
                break
        return self.curr.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)