class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        freq = [[] for _ in range(len(nums)+1)]
        for num, count in counts.items():
            freq[count].append(num)

        res = []
        for f in range(len(freq)-1, -1, -1):
            for val in freq[f]:
                res.append(val)
                if len(res) == k:
                    return res