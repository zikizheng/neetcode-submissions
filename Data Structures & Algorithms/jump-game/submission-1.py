class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        def dfs(i):
            if i == len(nums) - 1:
                return True
            elif i >= len(nums) or nums[i] == 0:
                return False
            for j in range(nums[i], 0, -1):
                memo[i + j] = dfs(i + j)
                if memo[i + j]:
                    return True
            return False
        return dfs(0)