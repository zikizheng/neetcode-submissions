class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [float('inf')] * amount
        for coin in coins:
            if 0 <= coin - 1 < amount:
                dp[coin - 1] = 1
        for i in range(amount):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i - coin] + 1, dp[i])
        return dp[-1] if not dp[-1] == float('inf') else -1