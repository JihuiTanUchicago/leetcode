class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s2 = s[::-1]
        dp = [[0 for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            dp[0][i] = 1 if s[0] == s2[i] else dp[0][i-1]
        for i in range(len(s)):
            dp[i][0] = 1 if s[i] == s2[0] else dp[i-1][0]
        for i in range(1, len(s)):
            for j in range(1, len(s)):
                if s[i] == s2[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]