class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(len(strs)):
                if len(strs[j]) <= i or strs[j][i] != c:
                    return prefix
            prefix += c
        return prefix