class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        def dfs(i, j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return
            if board[i][j] != "X":
                return
            board[i][j] = "O"
            nxt = [(i-1,j), (i+1,j), (i, j-1), (i, j+1)]
            for pos in nxt:
                dfs(*pos)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    dfs(i, j)
                    count += 1
        
        return count
            