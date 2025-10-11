class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        undirected_graph = defaultdict(list)
        edges = set()
        for i,j in connections:
            edges.add((i,j))
            undirected_graph[i].append(j)
            undirected_graph[j].append(i)
        visited = {0}
        count = 0
        def dfs(root):
            nonlocal undirected_graph, visited, count, edges
            for city in undirected_graph[root]:
                if city in visited:
                    continue
                if (root, city) in edges:
                    count += 1
                visited.add(city)
                dfs(city)
        dfs(0)
        return count