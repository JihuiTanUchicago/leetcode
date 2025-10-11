class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        i = 0
        while i < len(s):
            if s[i] == goal[0]:
                if i == 0:
                    if s == goal:
                        return True
                elif s[i:] + s[0:i] == goal:
                    return True
            i += 1
        return False