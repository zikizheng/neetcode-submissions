class Solution:
    def rob(self, nums: List[int]) -> int:
        l, r = 0, 0
        for num in nums:
            l, r = r, max(num + l, r)
        return r