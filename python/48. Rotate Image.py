class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for col in range(n):
            start, end = 0, n-1
            while start < end:
                matrix[start][col], matrix[end][col] = matrix[end][col], matrix[start][col]
                start += 1
                end -= 1
        
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        
# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         print(matrix)
#         for i in range(len(matrix)):
#             for j in range(i, len(matrix)):
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#         for i in range(len(matrix)):
#             matrix[i].reverse()