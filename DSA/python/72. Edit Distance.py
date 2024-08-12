class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        At word1[i] and word2[j],
        1) if word1[i] == word[j], skip
        2) if len(word1) < len(word2)
            a) if word1[i] != word2[j]
                i) replace word1[i] with word2[j], return 1 + minDistance(word1[i+1:], word2[j+1:])
                ii) insert word2[j] before word1[i], return 1 + minDistance(word1[i:], word2[j+1:])
        3) if len(word1) > len(word2)
            a) if word1[i] != word2[k]
                i) replace word1[i] with word2[j], return 1 + minDistance(word1[i+1:], word2[j+1:])
                ii) delete word1[i], return 1 + minDistance(word1[i+1:], word2[j:])
        3) if len(word1) == len(word2)
            a) if word1[i] != word2[j]
                i) replace word1[i] with word2[j], return 1 + minDistance(word1[i+1:], word2[j+1:])
                ii) delete word1[i], return 1 + minDistance(word1[i+1:], word2[j:])
                iii) insert word2[j] infront of word1
        """
        word1_len = len(word1)
        word2_len = len(word2)
        dp = [[0 for i in range(word2_len+1)] for j in range(word1_len+1)]
        for i in range(word1_len+1):
            dp[i][0] = i
        for i in range(word2_len+1):
            dp[0][i] = i
        for i in range(1, word1_len+1):
            for j in range(1, word2_len+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
        
        return dp[-1][-1]