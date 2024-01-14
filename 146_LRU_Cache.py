class ListNode:
    def __init__(self, val=0, key=None, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = ListNode()
        self.right = ListNode(0, None, None, self.left)
        self.left.next = self.right

    def get(self, key: int) -> int:
        if key in self.cache:
            self.insert(key, self.cache[key].val)
            return self.cache[key].val
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.capacity += 1

        self.insert(key, value)

        if self.capacity > 0:
            self.capacity -= 1
        else:
            self.cache.pop(self.right.prev.key)
            self.right.prev = self.right.prev.prev
            self.right.prev.next = self.right
    
    def insert(self, key, value):
        #print([x.val for x in self.cache.values()])
        if key in self.cache:
            self.cache[key].val = value
            self.cache[key].prev.next = self.cache[key].next
            self.cache[key].next.prev = self.cache[key].prev
            self.cache[key].next = self.left.next
            self.cache[key].prev = self.left
        else:
            self.cache[key] = ListNode(value, key, self.left.next, self.left) 
        self.left.next = self.cache[key]
        self.cache[key].next.prev = self.cache[key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
        


# Solution V2

class ListNode:
    def __init__(self, key=-1, val=-1, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = ListNode()
        self.right = ListNode()
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key in self.cache:
            self.insert(self.cache[key].key, self.cache[key].val)
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) == self.capacity and key not in self.cache:
            self.cache.pop(self.right.prev.key)
            self.right.prev = self.right.prev.prev
            self.right.prev.next = self.right
            
        self.insert(key, value)

    def insert(self, key, value):
        if key in self.cache:
            self.cache[key].val = value
            self.cache[key].next.prev = self.cache[key].prev
            self.cache[key].prev.next = self.cache[key].next
            self.cache[key].next = self.left.next
            self.cache[key].prev = self.left
        else:
            self.cache[key] = ListNode(key, value, self.left.next, self.left)
        self.left.next.prev = self.cache[key]
        self.left.next = self.cache[key]
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)