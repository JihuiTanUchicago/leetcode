class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        num_set = {i for i in range(1, len(grid) * len(grid)+1)}
        output = []
        for i in range(len(grid)):
            for j in range(len(grid)):
                val = grid[i][j]
                if val in num_set:
                    num_set.remove(val)
                else:
                    output.append(val)
        
        output.append(num_set.pop())
        return output
