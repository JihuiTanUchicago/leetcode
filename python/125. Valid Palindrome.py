class Solution:
    def isPalindrome(self, s: str) -> bool:
        header, trailer = 0, len(s)-1
        while header <= trailer:
            if not s[header].isalnum():
                header += 1
            elif not s[trailer].isalnum():
                trailer -= 1
            elif s[header].lower() == s[trailer].lower():
                header += 1
                trailer -= 1
            else:
                return False
        return True