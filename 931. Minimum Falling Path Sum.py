class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [[0 for i in range(len(matrix))] for j in range(len(matrix))]
        for i in range(len(matrix)):
            dp[0][i] = matrix[0][i]
        for i in range(1, len(matrix)):
            for j in range(len(matrix)):
                if j == 0:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + matrix[i][j]
                elif j == len(matrix) - 1:
                    dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]) + matrix[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i-1][j+1]) + matrix[i][j]
        return min(dp[-1])