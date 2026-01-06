class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_sell_prices = [float('-inf') for i in range(len(prices))]
        max_sell_price = float('-inf')
        for i in range(len(prices)-1, -1, -1):
            max_sell_prices[i] = max_sell_price
            max_sell_price = max(max_sell_price, prices[i])
        
        max_dif_prices = [max_sell_prices[i] - prices[i] for i in range(len(prices))]
        max_profit = max(max_dif_prices)
        if max_profit < 0:
            return 0
        return max_profit
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profits = [0 for i in range(len(prices))]
#         min_buy = prices[0]
#         for i in range(1, len(prices)):
#             profits[i] = prices[i] - min_buy
#             min_buy = min(min_buy, prices[i])
#         max_profit = max(profits)
#         if max_profit <= 0:
#             return 0
#         return max_profit
