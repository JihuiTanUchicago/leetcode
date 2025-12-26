from collections import defaultdict
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = defaultdict(lambda: defaultdict(lambda: -1))
        def dp(amount, i):
            if memo[amount][i] != -1:
                return memo[amount][i]
            elif amount == 0:
                memo[amount][i] = 1
            elif i == len(coins):
                memo[amount][i] = 0
            elif coins[i] > amount:
                memo[amount][i] = dp(amount, i+1)
            else:
                memo[amount][i] = dp(amount-coins[i], i) + dp(amount, i+1)
            return memo[amount][i]
        return dp(amount, 0)