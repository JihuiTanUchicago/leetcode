class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1]]
        def getCurrentRow(prevRow):
            curRow = [0 for i in range(len(prevRow)+1)]
            for i in range(len(curRow)):
                if i == 0 or i == len(curRow)-1:
                    curRow[i] = 1
                else:
                    curRow[i] = prevRow[i-1] + prevRow[i]
            return curRow
        for i in range(1, numRows):
            output.append(getCurrentRow(output[-1]))
        return output