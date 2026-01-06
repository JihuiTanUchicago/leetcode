class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        index_id = 2
        info_dict = {}
        boundary_dict = {}
        def dfs(i, j, visited):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return
            if grid[i][j] == 1:
                if index_id not in info_dict:
                    info_dict[index_id] = 0
                grid[i][j] = index_id
                info_dict[index_id] += 1
                nxt = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                for pos in nxt:
                    if pos not in visited:
                        visited.add(pos)
                        dfs(*pos, visited)
            else:
                if (i,j) not in boundary_dict:
                    boundary_dict[(i,j)] = set()
                boundary_dict[(i,j)].add(index_id)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j, {(i, j)})
                    index_id += 1
        
        max_size = 1
        for val in info_dict.values():
            max_size = max(val, max_size)
        for boundary in boundary_dict:
            cur_size = sum(info_dict[i] for i in boundary_dict[boundary]) + 1
            max_size = max(cur_size, max_size)

        return max_size

        

            