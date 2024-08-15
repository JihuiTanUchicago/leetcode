class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                neighbors = [(i-1,j),(i,j-1),(i+1,j),(i,j+1), (i-1,j-1),(i-1,j+1),(i+1,j-1),(i+1,j+1)]
                live_count = 0
                for n_i, n_j in neighbors:
                    if 0 <= n_i <= len(board)-1 and 0 <= n_j <= len(board[0])-1 and 1 <= board[n_i][n_j]:
                        live_count += 1
                if (live_count < 2 or live_count > 3) and board[i][j] == 1: board[i][j] = 2
                elif live_count == 3 and board[i][j] == 0: board[i][j] = -1
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2: board[i][j] = 0
                elif board[i][j] == -1: board[i][j] = 1
        