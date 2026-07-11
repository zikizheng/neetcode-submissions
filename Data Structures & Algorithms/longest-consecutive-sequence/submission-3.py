class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for num in numSet:
            if num - 1 not in numSet:
                l = 1
                while l + num in numSet:
                    l += 1
                res = max(res, l)
        return res