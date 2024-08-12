class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for i in range(amount+1)]
        dp[0] = 0
        coins.sort()
        for i in range(1, amount+1):
            for coin in coins:
                if i < coin:
                    continue
                dp[i] = min(dp[i], dp[i-coin] + 1)
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]