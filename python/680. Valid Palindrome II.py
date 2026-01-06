class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def match(i, j, wild_card):
            if i > j:
                return True
            if s[i] == s[j]:
                return match(i+1, j-1, wild_card)
            elif wild_card:
                return match(i+1, j, False) or match(i, j-1, False)
            else:
                return False

        return match(0, len(s)-1, True)
        
