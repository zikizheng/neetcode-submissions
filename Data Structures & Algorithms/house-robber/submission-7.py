class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [0] * len(nums)
        for i in range(len(nums)):
            if i > 1:
                s = max(nums[i] + memo[i - 2], memo[i - 1])
                memo[i] = s
            elif i == 1:
                memo[i] = max(nums[0], nums[1])
            elif i == 0:
                memo[i] = nums[0]
        return memo[i]