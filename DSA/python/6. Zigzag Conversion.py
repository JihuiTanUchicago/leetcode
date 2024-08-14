class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = ""
        for row in range(1, numRows+1):
            index = row - 1
            while index < len(s):
                result += s[index]
                if 1 < row < numRows:
                    zag_index = index + (numRows-row) * 2
                    if zag_index < len(s):
                        result += s[zag_index]
                index += numRows*2 - 2
        return result
                