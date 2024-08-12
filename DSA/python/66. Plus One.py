class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        print(digits)
        i = len(digits)-1
        while i >= 0 and digits[i] + 1 == 10:
            digits[i] = 0
            if i == 0:
                return [1] + digits
            i -= 1
        digits[i] += 1
        return digits