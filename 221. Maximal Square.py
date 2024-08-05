class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(1,len(matrix[i])):
                if matrix[i][j] != "0":
                    matrix[i][j] = str(int(matrix[i][j]) + min(int(matrix[i-1][j]), int(matrix[i][j-1]), int(matrix[i-1][j-1])))
        maximum = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if int(matrix[i][j]) > maximum:
                    maximum = int(matrix[i][j])
        return maximum ** 2