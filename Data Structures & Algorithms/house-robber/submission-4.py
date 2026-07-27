class Solution:
    def rob(self, nums: List[int]) -> int:
        l, r = 0, 0
        for num in nums:
            s = max(l + num, r)
            l = r
            r = s
        return r