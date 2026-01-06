class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = []
        digits = ""
        i = 0
        while i < len(s):
            c = s[i]
            while c.isdigit():
                digits += c
                i += 1
                if i == len(s):
                    break
                else:
                    c = s[i]
            if digits != "":
                d = int(digits)
                digits = ""
                if stack != []:
                    if stack[-1] == "*":
                        stack.pop()
                        left_num = stack.pop()
                        stack.append(left_num * d)
                    elif stack[-1] == "/":
                        stack.pop()
                        left_num = stack.pop()
                        stack.append(left_num // d)
                    else:
                        stack.append(d)
                    
                else:
                    stack.append(d)
            else:
                stack.append(c)
                i += 1

        num = stack[0]
        i = 1
        while i < len(stack):
            if stack[i] == "+":
                num += stack[i+1]
            else:
                num -= stack[i+1]
            i += 2
        return num
        

            
