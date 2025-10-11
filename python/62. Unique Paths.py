class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0 for i in range(n)] for j in range(m)]
        visited = [[0 for i in range(n)] for j in range(m)]
        visited[0][0] = 1
        paths[0][0] = 1
        stack = []
        next_stack = []
        if n > 1:
            stack.append([0,1])
            visited[0][1] = 1
        if m > 1:
            stack.append([1,0])
            visited[1][0] = 1
        while stack != []:
            row, col = stack.pop()
            if 0<col:
                paths[row][col] += paths[row][col-1]
            if 0<row:
                paths[row][col] += paths[row-1][col]
            if row < m-1 and visited[row+1][col] == 0:
                next_stack.append([row+1,col])
                visited[row+1][col] = 1
            if col < n-1 and visited[row][col+1] == 0:
                next_stack.append([row,col+1])
                visited[row][col+1] = 1
            if stack == []:
                stack = next_stack
                next_stack = []
        return paths[m-1][n-1]
