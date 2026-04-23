class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        buckets = [[] for i in range(len(nums)+1)]
        for i, n in seen.items():
            buckets[n].append(i)
        
        res = []
        for i in range(len(nums), 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res