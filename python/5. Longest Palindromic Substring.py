class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i, j):
            if i < 0 or j >= len(s):
                return (i+1, j-1)
            if s[i] == s[j]:
                return expand(i-1, j+1)
            else:
                return (i+1, j-1)

        max_index = (-1, -1)
        max_dist = 0
        for i in range(len(s)):
            a, b = expand(i, i)
            if b-a+1 > max_dist:
                max_index = (a, b)
                max_dist = b-a+1
        for i in range(len(s)-1):
            a, b = expand(i, i+1)
            if b-a+1 > max_dist:
                max_index = (a, b)
                max_dist = b-a+1

        a, b = max_index
        return s[a:b+1]