class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        temp = set()
        def dfs(i, j):
            temp.add((i,j))

            if i >= m or i < 0 or j >= n or j < 0 or board[i][j] == "X":
                return True
            # else it's "O"
            if i == m - 1 or i == 0 or j == n - 1 or j == 0:
                return False
            
            nxt = {(i+1,j), (i, j+1), (i-1, j), (i, j-1)}
            for pos in nxt:
                if pos in temp:
                    continue
                if dfs(*pos) == False:
                    return False
            return True
        
        visited = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    if (i,j) not in visited and dfs(i, j):
                        for pos in temp:
                            row, col = pos
                            board[row][col] = "X"
                    visited = visited | temp
                    temp = set()
        
                
            


        