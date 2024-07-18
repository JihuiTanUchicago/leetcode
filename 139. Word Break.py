class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(dp)):
            for word in wordDict:
                if len(word) <= i and word == s[i-len(word):i] and dp[i-len(word)]:
                    dp[i] = True
                    break
        return dp[-1]