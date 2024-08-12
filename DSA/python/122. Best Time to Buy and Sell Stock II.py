class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = [0 for i in range(len(prices))]
        for i in range(1, len(prices)):
            if prices[i] >= prices[i-1]:
                profits[i] = profits[i-1] + prices[i] - prices[i-1]
            else:
                profits[i] = profits[i-1]
        return profits[-1]