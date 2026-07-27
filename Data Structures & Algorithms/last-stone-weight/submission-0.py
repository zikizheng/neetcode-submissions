class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            l = -(heapq.heappop(heap))
            r = -(heapq.heappop(heap))
            if l < r:
                r = r - l
                heapq.heappush(heap, -r)
            elif l > r:
                l = l - r
                heapq.heappush(heap, -l)
        return -heap[0] if heap else 0