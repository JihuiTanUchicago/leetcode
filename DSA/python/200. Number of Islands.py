class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def checkEdge(i, j):
            if grid[i][j] == "0" or grid[i][j] == "2":
                return
            grid[i][j] = "2"
            if i > 0:
                checkEdge(i-1,j)
            if i < len(grid)-1:
                checkEdge(i+1,j)
            if j < len(grid[0])-1:
                checkEdge(i, j+1)
            if j > 0:
                checkEdge(i, j-1)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    checkEdge(i,j)
                    count += 1
        return count