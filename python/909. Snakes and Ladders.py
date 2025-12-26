import math
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        roll = 0
        n = len(board)
        current_level = [1]
        next_level = []
        visited = set()
        while current_level != []:
            current_position = current_level.pop()
            if current_position == n*n:
                return roll
            for i in range(1, 7):
                if current_position + i > n*n:
                    continue
                row = math.ceil((current_position+i) / n)
                b = (current_position+i) % n
                if row % 2 == 0:
                    col = -b
                else:
                    col = b - 1
                row = -row
                if board[row][col] != -1:
                    if board[row][col] not in visited:
                        next_level.append(board[row][col])
                        visited.add(board[row][col])
                elif current_position+i not in visited:
                    next_level.append(current_position+i)
                    visited.add(current_position+i)
            
            if current_level == []:
                current_level = next_level
                next_level = []
                roll += 1
        if n*n in visited:
            return roll
        else:
            return -1
