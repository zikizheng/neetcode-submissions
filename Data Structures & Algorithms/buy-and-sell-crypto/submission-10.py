class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        minBuy = prices[0]
        for price in prices:
            minBuy = min(price, minBuy)
            res = max(price - minBuy, res)
        return res