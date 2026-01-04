from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        connect_dict = defaultdict(set)
        for connection in connections:
            connect_dict[connection[0]].add(connection[1])
            connect_dict[connection[1]].add(connection[0])

        tin = [-1 for i in range(n)]
        low = [-1 for i in range(n)]
        output = []
        time = 0

        def dfs(node, parent):
            nonlocal time
            tin[node] = low[node] = time
            time += 1
            children = connect_dict[node]
            for child in children:
                if child == parent:
                    continue
                if tin[child] != -1:
                    low[node] = min(low[node], tin[child])
                else:
                    dfs(child, node)

                    low[node] = min(low[node], low[child])
                    if low[child] > tin[node]:
                        output.append([node, child])


        dfs(0, -1)

        return output
                
                    
            


