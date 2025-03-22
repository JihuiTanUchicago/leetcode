class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        # 4 Actions: 1) Buy, 2)Sell, 1)Hold Buy, 2) skip
        # 3 dimensions: number of days (i), number of transactions (j), canBuy/canSell (k)
        # dp[i][j][0] means on day i, j trasaction left, and can buy
        ## either today I sell, or yester I can buy but skip
        # dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
        # dp[i][j][1] means either I hold from yesterday, or I bought today)
        # dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])
        dp = [[[float('-inf') for k in range(2)] for j in range(k+1)] for i in range(len(prices))]
        dp[0][0][0] = 0
        dp[0][1][1] = -prices[0]

        for i in range(1,n):
            for j in range(k+1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
                if j > 0:
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])
        
        maxProfit = max(dp[len(prices)-1][j][0] for j in range(k+1))

        return maxProfit