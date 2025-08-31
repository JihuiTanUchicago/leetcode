from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        data = [i for i in range(1, n+1)]
        for comb in combinations(data, k):
            result.append(comb)
        return result