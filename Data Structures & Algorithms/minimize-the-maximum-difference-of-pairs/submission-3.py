class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0: return 0
        
        n = len(nums)
        nums.sort()
        
        dp = [float('inf')] * (p + 1)
        dp1 = [float('inf')] * (p + 1)
        dp2 = [float('inf')] * (p + 1)

        dp[0] = dp1[0] = dp2[0] = 0

        for i in range(n - 2, -1, -1):
            for pairs in range(1, p + 1):
                take = max(nums[i + 1] - nums[i], dp2[pairs - 1])
                skip = dp1[pairs]
                dp[pairs] = min(take, skip)

            dp2 = dp1[:]
            dp1 = dp[:]
            dp = [float('inf')] * (p + 1)
            dp[0] = 0

        return dp1[p]