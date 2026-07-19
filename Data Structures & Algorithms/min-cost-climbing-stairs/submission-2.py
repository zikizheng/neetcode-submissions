class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * 3
        for i in range(2, len(cost) + 1):
            dp[i % 3] = min(dp[i % 3 - 1] + cost[i - 1], dp[i % 3 - 2] + cost[i - 2])
        return dp[i % 3]