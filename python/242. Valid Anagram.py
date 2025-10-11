from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        t_counter = Counter(t)
        return Counter(s) - Counter(t) == {} and Counter(t) - Counter(s) == {}