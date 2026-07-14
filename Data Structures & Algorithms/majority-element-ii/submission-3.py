class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

            if len(count) <= 2:
                continue
            newCount = {}
            for i, c in count.items():
                if c > 1:
                    newCount[i] = count[i] - 1
            count = newCount
        res = []
        for c in count:
            if nums.count(c) > (len(nums) / 3):
                res.append(c)
        return res