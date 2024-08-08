class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(s) != len(pattern):
            return False
        pattern_dict = {}
        s_dict = {}
        for i in range(len(pattern)):
            if pattern_dict.get(pattern[i], "") == "" and s_dict.get(s[i], "") == "":
                pattern_dict[pattern[i]] = s[i]
                s_dict[s[i]] = pattern[i]
            elif pattern_dict.get(pattern[i], "") == "" or s_dict.get(s[i], "") == "":
                return False
            elif s_dict[s[i]] != pattern[i]:
                return False
        return True

