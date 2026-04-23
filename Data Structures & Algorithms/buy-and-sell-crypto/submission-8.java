class Solution {
    public int maxProfit(int[] prices) {
        int res = 0;
        int minBuy = prices[0];
        for (int price : prices) {
            int profit = price - minBuy;
            res = Math.max(res, profit);
            minBuy = Math.min(minBuy, price);
        }
        return res;
    }
}
