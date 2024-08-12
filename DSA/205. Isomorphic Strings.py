from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = defaultdict(list)
        t_dict = defaultdict(list)
        for i in range(len(s)):
            s_dict[s[i]].append(i)
            t_dict[t[i]].append(i)
        s_vals = list(s_dict.values())
        t_vals = list(t_dict.values())
        if s_vals == t_vals:
            return True
        else:
            return False