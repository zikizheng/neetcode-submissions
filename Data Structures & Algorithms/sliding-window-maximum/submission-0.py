class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        r = k - 1
        while r < len(nums):
            window = [-1 * n for n in nums[l:r+1]]
            heapq.heapify(window)
            res.append(-1 * heapq.heappop(window))
            r += 1
            l += 1
        return res