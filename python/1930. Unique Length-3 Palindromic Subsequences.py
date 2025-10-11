from collections import defaultdict
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        count = 0
        record_set = set()
        record = defaultdict(set)
        for i in range(len(s)):
            if s[i] in record_set:
                continue
            for j in range(len(s)-1, i+1, -1):
                if s[i] == s[j] and s[i] not in record_set:
                    count += len(set(s[i+1:j]))
                    break
            record_set.add(s[i])
            if len(record_set) == 26:
                break
        return count



