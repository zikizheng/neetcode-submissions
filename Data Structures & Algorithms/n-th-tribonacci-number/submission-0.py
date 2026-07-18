class Solution:
    def tribonacci(self, n: int) -> int:
        dp = {}
        def trib(n):
            if n == 1:
                return 1
            elif n == 0:
                return 0
            elif n == 2:
                return 1
            if n in dp:
                return dp[n] 
            dp[n] = trib(n-1) + trib(n-2) + trib(n-3)
            return dp[n]
        return trib(n)