class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        indexes = []
        for i in range(len(s)):
            c = s[i]
            if c == ")":
                _, prev_i = stack.pop()
                if stack == []:
                    indexes += [prev_i, i]
            else:
                stack.append((c, i))
        
        output = ""
        start = 0
        for i in range(len(s)):
            if indexes[start] != i:
                output += s[i]
            else:
                start += 1
        
        return output


