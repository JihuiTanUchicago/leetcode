class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        if num >= 1000:
            thousand = int(num / 1000)
            result += "M" * thousand
            num -= 1000 * thousand
        if 100 <= num < 1000:
            hundred = int(num / 100)
            if hundred == 9:
                result += "CM"
            elif hundred == 4:
                result += "CD"
            elif hundred >= 5:
                result += "D" + (hundred-5)*"C"
            else:
                result += hundred * "C"
            num -= 100 * hundred
        if 10 <= num < 100:
            ten = int(num / 10)
            if ten == 9:
                result += "XC"
            elif ten == 4:
                result += "XL"
            elif ten >= 5:
                result += "L" + (ten-5) * "X"
            else:
                result += ten * "X"
            num -= 10 * ten
        if 1 <= num < 10:
            if num == 9:
                result += "IX"
            elif num == 4:
                result += "IV"
            elif num >= 5:
                result += "V" + (num-5) * "I"
            else:
                result += num * "I"
        return result
            