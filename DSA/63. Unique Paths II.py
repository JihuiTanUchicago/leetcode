class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [[0 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]
        if obstacleGrid[0][0] == 0:
            dp[0][0] = 1
        for i in range(1, len(obstacleGrid)):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
        for i in range(1, len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = dp[0][i-1]
        for i in range(1, len(obstacleGrid)):
            for j in range(1,len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    continue
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        print(dp)
        return dp[-1][-1]