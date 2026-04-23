class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = [[] for _ in range(len(nums)+1)]
        seen = {}
        res = []
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        for num, count in seen.items():
            counts[count].append(num)
        p = 0
        for i in range(len(counts)-1, -1, -1):
            for num in counts[i]:
                res.append(num)
                if len(res) == k:
                    return res