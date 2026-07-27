class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [-i for i in nums]
        heapq.heapify(self.heap)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        heap = [i for i in self.heap]
        res = 0
        for i in range(self.k):
            res = -1 * heapq.heappop(heap)
        return res