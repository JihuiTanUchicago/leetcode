class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        queue = []
        visited = set()
        found = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue.append((i,j))
                    found = True
                    break
            if found:
                break

        while queue != []:
            i, j = queue.pop()
            visited.add((i,j))
            grid[i][j] = 2
            nxt = [(i+1,j), (i-1,j), (i,j+1), (i, j-1)]
            for ele in nxt:
                a, b = ele
                if (a,b) not in visited and 0 <=a<len(grid) and 0<=b<len(grid[0]) and grid[a][b] == 1:
                    queue.append(ele)
        
        queue = visited
        next_queue = set()
        distance = 0
        visited = set()

        while len(queue) > 0:
            i, j = queue.pop()
            visited.add((i,j))
            nxt = [(i+1,j), (i-1,j), (i,j+1), (i, j-1)]
            for ele in nxt:
                a, b = ele
                if (a,b) not in visited and 0 <=a<len(grid) and 0 <=b<len(grid[0]):
                    if grid[a][b] == 0:
                        next_queue.add(ele)
                    elif grid[a][b] == 1:
                        return distance
            
            if len(queue) == 0:
                queue = next_queue
                next_queue = set()
                distance += 1
                

