class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [-1] * (n+1)
        def climb(i):
            if i < 2:
                memo[i] = 0
                return memo[i]
            if memo[i] != -1:
                return memo[i]
            memo[i] = min(climb(i-1) + cost[i-1], climb(i-2) + cost[i-2])
            return memo[i]
        return climb(n)