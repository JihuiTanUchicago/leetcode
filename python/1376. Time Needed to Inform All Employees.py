from collections import defaultdict
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subbordinates = defaultdict(list)
        for i in range(len(manager)):
            higherup = manager[i]
            subbordinates[higherup].append(i)
        
        def dfs(i):
            if subbordinates[i] == []:
                return informTime[i]
            max_time = float('-inf')
            for sub in subbordinates[i]:
                max_time = max(max_time, dfs(sub))
            return max_time + informTime[i]
        
        return dfs(headID)
        