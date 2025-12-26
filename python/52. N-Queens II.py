class Solution:
    def totalNQueens(self, n: int) -> int:
        hor = set()
        ver = set()
        diag = set()
        anti_diag = set()

        count = 0
        def dfs(ith_queen):
            if ith_queen == n:
                nonlocal count
                count += 1
                return
            i = ith_queen
            if i in hor:
                return
            for j in range(n):
                if j not in ver and (i+j) not in diag and (j-i) not in anti_diag:
                    hor.add(i)
                    ver.add(j)
                    diag.add(i+j)
                    anti_diag.add(j-i)
                    dfs(ith_queen+1)
                    hor.remove(i)
                    ver.remove(j)
                    diag.remove(i+j)
                    anti_diag.remove(j-i)
        dfs(0)
        return count