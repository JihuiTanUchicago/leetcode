class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        def dfs(i, visited):
            visited.add(i)
            if i == n-1:
                visited.remove(i)
                return [[n-1]]
            if len(graph[i]) == 0:
                visited.remove(i)
                return [[]]
            candidates = graph[i]
            result = []
            for candidate in candidates:
                if candidate in visited:
                    continue
                paths = dfs(candidate, visited)
                for path in paths:
                    if path != []:
                        result.append([i] + path)
            visited.remove(i)
            return result
        return dfs(0, set())
            

