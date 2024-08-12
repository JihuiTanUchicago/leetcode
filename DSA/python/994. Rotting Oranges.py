class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count_fresh = 0
        rottens = []
        next_rottens = []
        minute = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    grid[i][j] = 3 #visited
                    rottens.append([i,j])
                if grid[i][j] == 1:
                    count_fresh += 1
        if count_fresh == 0:
            return 0
        while rottens != []:
            row, col = rottens.pop()
            if 0<=row-1 and grid[row-1][col] == 1:
                count_fresh -= 1
                grid[row-1][col] = 3
                next_rottens.append([row-1,col])
            if row+1<len(grid) and grid[row+1][col] == 1:
                count_fresh -= 1
                grid[row+1][col] = 3
                next_rottens.append([row+1,col])
            if 0<=col-1 and grid[row][col-1] == 1:
                count_fresh -= 1
                grid[row][col-1] = 3
                next_rottens.append([row,col-1])
            if col+1<len(grid[0]) and grid[row][col+1] == 1:
                count_fresh -= 1
                grid[row][col+1] = 3
                next_rottens.append([row,col+1])
            if count_fresh == 0:
                return minute + 1
            if rottens == []:
                rottens = next_rottens
                next_rottens = []
                minute += 1
        return -1
            
