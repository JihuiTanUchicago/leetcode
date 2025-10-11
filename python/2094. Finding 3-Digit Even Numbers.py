class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digits.sort()
        ans_set = set()
        for i in range(len(digits)):
            if digits[i] == 0:
                continue
            if i != 0 and digits[i-1] == digits[i]:
                continue
            firstDigit = digits[i]
            for j in range(len(digits)):
                if j == i:
                    continue
                secondDigit = digits[j]
                for k in range(len(digits)):
                    if k == i or k == j:
                        continue
                    if digits[k] % 2 != 0:
                        continue
                    thirdDigit = digits[k]
                    num = 100 * firstDigit + 10 * secondDigit + thirdDigit
                    ans_set.add(num)
        return sorted(list(ans_set))
