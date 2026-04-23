class node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        newNode = node(val)
        
        newNode.next = self.head.next
        self.head.next = newNode
        if not newNode.next:
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        newNode = node(val)
        self.tail.next = newNode
        self.tail = newNode

    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0
        while curr:
            if i == index and curr.next:
                curr.next = curr.next.next
                if not curr.next:
                    self.tail = curr
                return True
            i += 1
            curr = curr.next
        return False

    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res