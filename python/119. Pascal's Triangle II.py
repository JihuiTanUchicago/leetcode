import math
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        n = rowIndex
        total_factorial = math.factorial(n)
        output = []
        for i in range(n+1):
            denominator_1 = math.factorial(n-i)
            denominator_2 = math.factorial(i)
            output.append(int(total_factorial / (denominator_1 * denominator_2)))
        return output