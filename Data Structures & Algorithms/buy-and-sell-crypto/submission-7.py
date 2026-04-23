class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minBuy = prices[0]
        for price in prices:
            profit = price - minBuy
            res = max(res, profit)
            minBuy = min(minBuy, price)
        return res