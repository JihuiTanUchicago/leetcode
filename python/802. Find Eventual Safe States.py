class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe_nodes = set()
        visited = set()
        def dfs(i):
            if i in visited:
                if i not in safe_nodes:
                    return False
                else:
                    return True
            
            visited.add(i)
            if i in safe_nodes:
                return True
            outs = graph[i]
            if outs == []:
                safe_nodes.add(i)
                return True
            
            for out in outs:
                if dfs(out) == False:
                    return False
            safe_nodes.add(i)
            return True

        for i in range(len(graph)):
            dfs(i)
        
        return sorted(list(safe_nodes))
            
        