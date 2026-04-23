class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [] * capacity
        self.length = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.arr = self.arr + ([] * self.capacity)
            self.capacity *= 2
        self.arr.append(n)
        self.length += 1

    def popback(self) -> int:
        res = self.arr[self.length-1]
        self.arr[self.length-1] = None
        self.length -= 1
        return res

    def resize(self) -> None:
        self.arr = self.arr + [] * capacity
        capacity *= 2


    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity