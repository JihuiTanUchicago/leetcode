from itertools import combinations
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(start, val, ls):
            if val == target:
                result.append(ls)
                return
            if val > target:
                return
            for i in range(start, len(candidates)):
                dfs(i, val+candidates[i], ls+[candidates[i]])
        dfs(0, 0, [])
        return list(result)