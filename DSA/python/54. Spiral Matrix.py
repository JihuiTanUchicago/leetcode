class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        i,j = 0, 0
        direction = 0
        hor, ver = len(matrix[0]), len(matrix)
        area = len(matrix)*len(matrix[0])
        for start in range(area):
            result.append(matrix[j][i])
            if direction == 0 and i != hor-1:
                i += 1
            elif direction == 0 and i == hor-1:
                j += 1
                direction = 1
            elif direction == 1 and j != ver-1:
                j += 1
            elif direction == 1 and j == ver-1:
                i -= 1
                direction = 2
                ver -= 1
            elif direction == 2 and i != len(matrix[0]) - hor:
                i -= 1
            elif direction == 2 and i == len(matrix[0]) - hor:
                j -= 1
                direction = 3
                hor -= 1
            elif direction == 3 and j != len(matrix) - ver:
                j -= 1
            elif direction == 3 and j == len(matrix) - ver:
                i += 1
                direction = 0
        
        return result