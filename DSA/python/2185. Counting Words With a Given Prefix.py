class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for i in range(len(words)):
            if len(words[i]) >= len(pref) and words[i][:len(pref)] == pref:
                count += 1
        return count