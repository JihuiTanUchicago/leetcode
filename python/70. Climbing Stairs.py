class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for i in range(n+1)]
        dp[1] = 1
        dp[0] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[-1]

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         dp = [0 for i in range(n+1)]
#         dp[0] = 0
#         dp[1] = 1
#         dp[2] = 2
#         for i in range(3, n+1):
#             dp[i] = dp[i-1] + dp[i-2]
#         return dp[-1]
        