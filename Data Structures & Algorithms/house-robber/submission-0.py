class Solution:
    def __init__(self):
        self.memo = {}

    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            self.memo[len(nums)] = max(nums)
            return self.memo[len(nums)]
        if len(nums) in self.memo:
            return self.memo[len(nums)]
        self.memo[len(nums)] = max(nums[0] + self.rob(nums[2:len(nums)]), self.rob(nums[1:len(nums)]))
        return self.memo[len(nums)]