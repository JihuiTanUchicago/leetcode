class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = [0 for i in range(len(prices))]
        min_buy = prices[0]
        for i in range(1, len(prices)):
            profits[i] = prices[i] - min_buy
            min_buy = min(min_buy, prices[i])
        max_profit = max(profits)
        if max_profit <= 0:
            return 0
        return max(profits)
