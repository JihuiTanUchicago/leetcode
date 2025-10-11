class Solution:
    def isHappy(self, n: int) -> bool:
        records = set()
        while n != 1:
            summation = 0
            str_n = str(n)
            for num in str_n:
                digit = int(num)
                summation += digit * digit
            if summation in records:
                return False
            else:
                records.add(summation)
            n = summation
        return True
