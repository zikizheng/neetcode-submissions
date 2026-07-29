class ListNode:
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.start = ListNode()
        self.end = ListNode()
        self.start.next = self.end
        self.end.prev = self.start

        self.capacity = capacity
        self.cache = {}

    def insert(self, node):
        node.next = self.end
        node.prev = self.end.prev
        self.end.prev.next = node
        self.end.prev = node
        

    def replace(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.replace(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.replace(self.cache[key])
            self.cache[key].val = value
        else:
            self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            del self.cache[self.start.next.key]
            self.replace(self.start.next)
