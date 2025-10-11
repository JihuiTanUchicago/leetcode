class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        #buy, sell, or do nothing at price[i]
        """
        Need to keep track of max_profit from prices[0] to prices[-1]
        1) To buy or not to buy: use a `action_buy` to keep track of max profit
        2) To sell or not to sell: use a `action_sell` to keep track of max profit
        """
        action_buy = -prices[0]
        action_sell = 0
        for i in range(1, len(prices)):
            action_buy = max(action_buy, action_sell-prices[i])
            action_sell = max(action_sell, action_buy + prices[i] - fee)
        
        return action_sell