class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        
        freq = [[] for _ in range(len(nums) + 1)]
        for val, count in seen.items():
            freq[count].append(val)
        
        res = []
        for i in range(len(freq) - 1, -1, -1):
            for val in freq[i]:
                res.append(val)
                if len(res) == k:
                    return res