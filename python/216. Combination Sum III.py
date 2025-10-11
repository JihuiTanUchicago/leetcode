class Solution:
    def getSum(self, lower_bound: int, k: int, n: int) -> List[List[int]]:
        if k == 1:
            if lower_bound <= n <= 9: return [[n]]
            else: return []
        results = []
        for i in range(lower_bound, 10):
            cur_results = self.getSum(i+1, k-1, n-i)
            for j in range(len(cur_results)):
                cur_results[j].append(i)
            results += cur_results
        return results
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return self.getSum(1, k, n)

    