class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0 for i in range(len(questions)+1)]
        for i in range(len(questions)-1, -1 , -1):
            jump_score = dp[i+1+questions[i][1]] if i+1+questions[i][1] < len(dp) else 0
            dp[i] = max(dp[i+1], jump_score + questions[i][0])
        
        return dp[0]