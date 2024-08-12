class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {"I":1, "V":5, "X":10, "L":50, "C":100,"D":500,"M":1000}
        summation = dictionary[s[-1]]
        for i in range(len(s)-2, -1, -1):
            if dictionary[s[i+1]] > dictionary[s[i]]:
                summation -= dictionary[s[i]]
            else:
                summation += dictionary[s[i]]
        return summation
