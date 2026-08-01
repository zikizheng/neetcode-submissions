class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
                return max(nums)
        def dfs(n):
            if len(n) <= 2:
                return max(n)
            two, one = n[0], max(n[0], n[1])
            for i in range(2, len(n)):
                two, one = one, max(one, two + n[i])
            return one
        return max(dfs(nums[:-1]), dfs(nums[1:]))