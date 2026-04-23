class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minBuy = prices[0]
        for price in prices:
            res = max(res, price - minBuy)
            minBuy = min(minBuy, price)
        return res