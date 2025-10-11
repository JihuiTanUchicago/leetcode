class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        directed_graph = defaultdict(set)
        for i in range(len(values)):
            l_var, r_var = equations[i]
            val = values[i]
            directed_graph[l_var].add((r_var, val))
            directed_graph[r_var].add((l_var, 1/val))
        
        visited = set()
        def dfs(root, target):
            nonlocal directed_graph, visited
            visited.add(root)
            if len(directed_graph[root]) != 0:
                for var, val in directed_graph[root]:
                    if var == target:
                        return val
                    elif var not in visited:
                        result = val * dfs(var, target)
                        if result != 0:
                            return result
            return 0

        outputs = []
        for a, b in queries:
            output = dfs(a,b)
            if output == 0:
                output = -1.0
            outputs.append(output)
            visited = set()

        return outputs