class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res, maxCount = 0, 0
        for num in nums:
            count[num] = count.get(num, 0) + 1
            res = num if count[num] > maxCount else res
            maxCount = max(maxCount, count[num])
        return res