class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        frequency = [[] for _ in range(len(nums)+1)]
        for num, freq in count.items():
            frequency[freq].append(num)
        res = []
        for i in range(len(frequency)-1,-1,-1):
            for f in frequency[i]:
                res.append(f)
                if len(res) == k:
                    return res
