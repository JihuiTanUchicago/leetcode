class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            cur = trie
            for c in word:
                if cur.get(c, None) is None:
                    cur[c] = {}
                cur = cur[c]
            cur["END"] = word

        found_set = set()
        m = len(board)
        n = len(board[0])
        def dfs(i, j, cur, visited):
            if "END" in cur:
                found_set.add(cur["END"])
            if i >= m or i < 0 or j >= n or j < 0:
                return
            c = board[i][j]
            if c in cur:
                cur = cur[c]
                if "END" in cur:
                    found_set.add(cur["END"])
                next_moves = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                for move in next_moves:
                    if move not in visited:
                        dfs(*move, cur, visited | {move})

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie, {(i,j)})
                if len(words) == len(found_set):
                    break
        return list(found_set)
