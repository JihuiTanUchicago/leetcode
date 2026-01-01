from collections import deque, defaultdict
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        reds = defaultdict(set)
        blues = defaultdict(set)
        for edge in redEdges:
            a, b = edge
            reds[a].add(b)
        for edge in blueEdges:
            a, b = edge
            blues[a].add(b)
        
        shortest = defaultdict(lambda: float('inf'))
        
        queue = deque([(0, 0, -1), (0, 0, 1)])
        visited = set()
        while queue:
            node, step, color = queue.popleft()
            visited.add((node, color))
            shortest[node] = min(step, shortest[node])
            if color == -1: #red
                connects = blues[node]
            else:
                connects = reds[node]
            for connect in connects:
                if (connect, color * -1) in visited:
                    continue
                queue.append((connect, step+1, color * -1))
        
        output = []
        for i in range(n):
            if shortest[i] == float('inf'):
                output.append(-1)
            else:
                output.append(shortest[i])
        
        return output
