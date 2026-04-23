class DynamicArray:
    
    def __init__(self, capacity: int):
        self.length = 0;
        self.capacity = capacity;
        self.arr = []

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        self.arr.append(n)
        self.length += 1

    def popback(self) -> int:
        if self.length > 0:
            self.length -= 1
        return self.arr[self.length]

    def resize(self) -> None:
        self.capacity *= 2
        newArr = []
        for n in self.arr:
            newArr.append(n)
        self.arr = newArr


    def getSize(self) -> int:
        return self.length
        
    def getCapacity(self) -> int:
        return self.capacity