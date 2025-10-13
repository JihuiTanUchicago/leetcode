from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        for i in range(len(nums)+1):
            for comb in combinations(nums, i):
                results.append(comb)
        return results