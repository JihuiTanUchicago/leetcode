class Solution:
    def makeGood(self, s: str) -> str:
        s = list(s)
        stack = []
        stack.append([0, s[0]])
        for i in range(1, len(s)):
            if stack != [] and stack[-1][1] != s[i] and stack[-1][1].lower() == s[i].lower():
                s[stack[-1][0]] = "*"
                s[i] = "*"
                stack.pop()
            else:
                stack.append([i,s[i]])
        return ("".join(s)).replace("*", "")
            
        