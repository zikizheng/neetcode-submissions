class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        sec = 0
        for num in nums:
            if num == 1:
                sec += 1
                res = max(sec, res)
            else:
                sec = 0
        return res