import math
class Solution:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.N = float('inf')
        self.positions = []
        self.non_zero_count_cumulative = [0]

    def minTransfers(self, transactions: List[List[int]]) -> int:
        positions = [0 for i in range(12)]
        for transaction in transactions:
            from_i, to_i, amount_i = transaction
            positions[from_i] -= amount_i
            positions[to_i] += amount_i
        
        adjusted_positions = []
        for position in positions:
            if position != 0:
                adjusted_positions.append(position)
        self.positions = adjusted_positions
        self.N = len(adjusted_positions)
        for i in range(self.N):
            if self.positions[i] != 0:
                self.non_zero_count_cumulative.append(self.non_zero_count_cumulative[i] + 1)
            else:
                self.non_zero_count_cumulative.append(self.non_zero_count_cumulative[i-1])
        self.non_zero_count_cumulative.pop(0)
        return self.explore(0, 0)
    
    def explore(self, index, count):
        if index == self.N:
            return count
        elif self.positions[index] == 0:
            return self.explore(index+1, count)
        else:
            local_min_count = float('inf')
            for i in range(index+1, self.N):
                if self.positions[i] * self.positions[index] < 0:
                    self.positions[i] += self.positions[index]
                    local_min_count = min(local_min_count, self.explore(index+1, count+1))
                    self.positions[i] -= self.positions[index]
                    if local_min_count == math.ceil(self.non_zero_count_cumulative[i]) / 2:
                        return local_min_count
            return local_min_count
            
