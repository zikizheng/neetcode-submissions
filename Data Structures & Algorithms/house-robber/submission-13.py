class Solution:
    def __init__(self):
        self.mp = {}
    def rob(self, nums: List[int]) -> int:
        if tuple(nums) in self.mp:
            return self.mp[tuple(nums)]
        if len(nums) <= 2:
            self.mp[tuple(nums)] = max(nums)
            return self.mp[tuple(nums)]
        self.mp[tuple(nums)] = max(nums[-1] + self.rob(nums[:-2]), self.rob(nums[:-1]))
        return self.mp[tuple(nums)]