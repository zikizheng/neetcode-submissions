class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 2:
            return 1 if n != 0 else 0
        
        dp = [0, 1, 1]

        for i in range(3, n+1):
            dp[i % 3] = dp[0] + dp[1] + dp[2]
        return dp[n % 3]