from collections import Counter

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            s_counter = Counter(s)
            if s_counter.most_common(1)[0][1] >= 2:
                return True
            return False

        s_c, goal_c = None, None
        happened = False
        for i in range(len(s)):
            if s[i] != goal[i]:
                if happened:
                    return False
                if s_c is None and goal_c is None:
                    s_c = goal[i]
                    goal_c = s[i]
                elif s[i] != s_c or goal[i] != goal_c:
                    return False
                else:
                    happened = True

        if happened == False:
            return False 
        return True