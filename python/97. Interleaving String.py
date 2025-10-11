class Solution:
    @cache
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if s1 == "" and s2 == "" and s3 == "":
            return True
        condition = False
        if s1 != "" and s1[0] == s3[0]:
            condition = condition or self.isInterleave(s1[1:], s2, s3[1:])
        if s2 != "" and s2[0] == s3[0]:
            condition = condition or self.isInterleave(s1, s2[1:], s3[1:])
            
        return condition
        