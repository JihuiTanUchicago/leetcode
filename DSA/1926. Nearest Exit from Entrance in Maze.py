class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        steps = 0
        maze[entrance[0]][entrance[1]] = '/'
        cells = [[entrance[0],entrance[1]]]
        next_cells = []
        row_len = len(maze)
        col_len = len(maze[0]) 
        while cells != []:
            row,column = cells.pop()
            if steps != 0 and (row == 0 or row == row_len-1 or column==0 or column==col_len-1):
                return steps
            if 0<=row-1 and maze[row-1][column] == '.':
                maze[row-1][column] = '/'
                next_cells.append([row-1, column])
            if row+1 < len(maze) and maze[row+1][column] == '.':
                maze[row+1][column] = '/'
                next_cells.append([row+1, column])
            if 0<=column-1 and maze[row][column-1]=='.':
                maze[row][column-1] = '/'
                next_cells.append([row, column-1])
            if column+1<len(maze[0]) and maze[row][column+1] == '.':
                maze[row][column+1] = '/'
                next_cells.append([row,column+1])
            if cells == []:
                cells = next_cells
                next_cells = []
                steps += 1
        return -1
            
        