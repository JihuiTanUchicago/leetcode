class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for i in range(amount+1)]
        dp[0] = 0

        for i in range(1, amount + 1):
            min_coins = float('inf')
            for coin in coins:
                if i - coin < 0:
                    continue
                min_coins = min(min_coins, dp[i-coin])
            dp[i] = min_coins + 1

        if dp[amount] == float('inf'):
            return -1
        return dp[amount]

# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = [float('inf') for i in range(amount+1)]
#         dp[0] = 0
#         for coin in coins:
#             for i in range(coin, amount+1):
#                 dp[i] = min(dp[i], dp[i-coin] + 1)
        
#         return dp[amount] if dp[amount] != float('inf') else -1
# # class Solution:
# #     def coinChange(self, coins: List[int], amount: int) -> int:
# #         dp = [float('inf') for i in range(amount+1)]
# #         dp[0] = 0
# #         coins.sort()
# #         for i in range(1, amount+1):
# #             for coin in coins:
# #                 if i < coin:
# #                     continue
# #                 dp[i] = min(dp[i], dp[i-coin] + 1)
# #         if dp[-1] == float('inf'):
# #             return -1
# #         return dp[-1]