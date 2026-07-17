class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        res = 0
        for p in prices:
            minBuy = min(minBuy, p)
            profit = p - minBuy
            res = max(res, profit)
        return res