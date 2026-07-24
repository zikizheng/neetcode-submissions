class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        orderedCounts = [[] for _ in range(max(counts.values()) + 1)]
        for num, count in counts.items():
            orderedCounts[count].append(num)
        
        res = []
        for i in range(len(orderedCounts) - 1, -1, -1):
            for frequency in orderedCounts[i]:
                res.append(frequency)
                if len(res) == k:
                    return res