class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        vert_top, vert_bottom = 0, len(matrix)-1
        possible_horizontal_index = -1
        while vert_top <= vert_bottom:
            mid = (vert_top + vert_bottom) // 2
            if matrix[mid][0] < target:
                possible_horizontal_index = mid
                vert_top = mid + 1
            elif matrix[mid][0] > target:
                vert_bottom = mid - 1
            else:
                return True
        
        if possible_horizontal_index == -1:
            return False

        
        hor_left, hor_right = 0, len(matrix[0])-1
        while hor_left <= hor_right:
            mid = (hor_left + hor_right) // 2
            if matrix[possible_horizontal_index][mid] < target:
                hor_left = mid + 1
            elif matrix[possible_horizontal_index][mid] > target:
                hor_right = mid - 1
            else:
                return True
        return False