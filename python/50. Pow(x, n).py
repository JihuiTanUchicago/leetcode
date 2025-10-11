class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if x == 0 or x == 1:
            return x
        if n < 0:
            x = 1/x
            n = abs(n)
        base = 1
        while n != 0:
            if n % 2 == 1:
                base *= x
                n -= 1
            x *= x
            n //= 2
        return base
