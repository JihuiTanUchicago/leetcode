class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        sign = 1
        num = 0
        has_sign = False

        for c in s:
            if not has_sign and (c == '-' or c == '+'):
                has_sign = True
                sign = 1 if c == '+' else -1
            elif c.isnumeric():
                has_sign = True
                num = num*10 + int(c)
            else:
                break

        num = num * sign
        if sign == 1 and num > 2 ** 31 -1 :
            return 2 ** 31 - 1
        elif num < -(2 ** 31):
            return -(2 ** 31)
        return num
            