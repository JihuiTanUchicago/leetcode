"""
some note for solving dynamic programming problems.
Start with a brute force solution and identify if there's any overlap.(the brute force solution is often a recursion)
Then develop a memorization mechanism for the overlap.
Use a complex enough example to outline the input/output of the brute force solution
Try to replace the input/output with a dp list(either 1d or multi-dimension)
Once you replace the entire input/output stream with a dp list, a dp solution should be clear enough
Then write it out!
"""
class Solution:
    @cache
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)]
        for i in range(len(s)+1):
            dp[i][0] = 1
        for j in range(1, len(t)+1):
            for i in range(j, len(s)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        """ 
        babgbag, bag, func(babgba,ba), func(bab, ba) | dp[7][3] = dp[6][2] + dp[3][2]
            - babgba, ba, func(babgb, b), func(b,b) | dp[6][2] = dp[5][1] + dp[1][1]
                -babgb,b, func(babg, ""), func(ba,""), func("", "") dp[5][1] = dp[4][0] + dp[2][0] + dp[0][0]
                    - babg,"", return 1 } dp[4][0] = 1
                    - ba, "", return 1 | dp[2][0] = 1
                    - "", "", return 1 | dp[0][0] = 1
                - b,b, func("", "") dp[1][1] = dp[0][0]
                    - dp[0][0] = 1
            -bab, ba, func(b, b) dp[3][2] = dp[1][1]
                - b,b, func("","") dp[1][1] = dp[0][0]
                    dp[0][0] = 1
        """

        
        """
        if t == "":
            return 1
        elif s == "":
            return 0
        count = 0
        for i in range(len(s)):
            if s[i] == t[-1]:
                count += self.numDistinct(s[:i], t[:-1])
        """
        return dp[-1][-1]
