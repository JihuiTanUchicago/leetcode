class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        i = 1
        while i <= n:
            num = i
            while num % 5 == 0:
                count += 1
                num = num/5
            i += 1
        return count