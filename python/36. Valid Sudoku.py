class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #verify sub-boxes first
        for m in range(9):
            fill_set = set()
            row, col = (m//3)*3, (m%3)*3
            for i in range(3):
                for j in range(3):
                    if board[row+i][col+j] != ".":
                        if board[row+i][col+j] in fill_set:
                            return False
                        fill_set.add(board[row+i][col+j])
        #verify rows and cols
        for i in range(9):
            row_set = set()
            col_set = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row_set:
                        return False
                    row_set.add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in col_set:
                        return False
                    col_set.add(board[j][i])
        return True

