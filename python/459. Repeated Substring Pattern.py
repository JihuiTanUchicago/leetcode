class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        t = s + s
        t = t[1:-1]
        if s in t:
            return True
        return False