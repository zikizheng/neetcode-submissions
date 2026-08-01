class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(nums):
            two, one = 0, 0
            for num in nums:
                two, one = one, max(one, two + num)
            return one
        return max(nums[0], dfs(nums[:-1]), dfs(nums[1:]))