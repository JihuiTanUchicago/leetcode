class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        one_score = 0
        zero_score = 0
        for i in range(len(s)):
            if s[i] == "1":
                one_score += 1
        for i in range(len(s)-1):
            if s[i] == "0":
                zero_score += 1
            else:
                one_score -= 1
            max_score = max(zero_score + one_score, max_score)
        return max_score
        