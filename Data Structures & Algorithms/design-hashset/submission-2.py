class MyHashSet:

    def __init__(self):
        self.st = [False] * (10 ** 6)

    def add(self, key: int) -> None:        
        self.st[key] = True

    def remove(self, key: int) -> None:
        self.st[key] = False

    def contains(self, key: int) -> bool:
        return self.st[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)