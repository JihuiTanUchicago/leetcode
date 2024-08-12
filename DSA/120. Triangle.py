import copy
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = copy.deepcopy(triangle)
        for i in range(len(triangle)):
            for j in range(len(triangle[i])):
                dp[i][j] = 0
        dp[0][0] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == len(triangle[i]) - 1:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
        return min(dp[-1])