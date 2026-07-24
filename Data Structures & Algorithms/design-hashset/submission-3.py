class ListNode:
    def __init__(self, val = 0):
        self.val = val
        self.next = None

class MyHashSet:

    def __init__(self):
        self.st = [ListNode()] * (10**4)

    def add(self, key: int) -> None:        
        curr = self.st[key % (10**4)]
        while curr.next:
            if curr.next.val == key:
                return
            curr = curr.next
        curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        curr = self.st[key % (10**4)]
        while curr.next:
            if curr.next.val == key:
                break
            curr = curr.next
        curr.next = curr.next.next if curr.next else None

    def contains(self, key: int) -> bool:
        curr = self.st[key % (10**4)]
        while curr.next:
            if curr.next.val == key:
                return True
            curr = curr.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)