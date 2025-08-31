class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def visit(i, j, word_index):
            if i >= len(board) or i < 0:
                return False
            if j >= len(board[0]) or j < 0:
                return False
            if (i, j) in visited:
                return False
            if board[i][j] == word[word_index]:
                if word_index+1 == len(word):
                    return True
                visited.add((i,j))
                if not (visit(i+1,j,word_index+1) or 
                        visit(i-1,j,word_index+1) or 
                        visit(i,j+1,word_index+1) or 
                        visit(i,j-1,word_index+1)):
                    visited.remove((i,j))
                    return False
                return True
        for i in range(len(board)):
            for j in range(len(board[0])):
                if visit(i, j, 0):
                    return True
        return False
