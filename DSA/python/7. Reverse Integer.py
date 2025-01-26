class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2 ** 31 - 1
        sign = -1 if x < 0 else 1
        rev_num, x = 0, abs(x)
        while x != 0:
            remainder = x % 10
            x = x // 10
            rev_num = 10 * rev_num + remainder
            if rev_num > INT_MAX:
                return 0
        return rev_num * sign
