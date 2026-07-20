class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0: return 0
        
        n = len(nums)
        nums.sort()
        dp = [[float('inf')] * (p + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0

        for i in range(n - 2, -1, -1):
            for pairs in range(1, p + 1):
                take = float('inf')
                if i + 1 < n:
                    take = max(nums[i + 1] - nums[i], dp[i+2][pairs-1])
                
                skip = dp[i+1][pairs]
                dp[i][pairs] = min(take, skip)
        
        return dp[0][p]