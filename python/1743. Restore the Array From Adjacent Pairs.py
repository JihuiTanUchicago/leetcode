from collections import defaultdict
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adj_dict = defaultdict(set)
        for pair in adjacentPairs:
            a, b = pair
            adj_dict[a].add(b)
            adj_dict[b].add(a)
        
        start = None
        for num in adj_dict:
            if len(adj_dict[num]) == 1:
                start = num
        
        n = len(adjacentPairs) + 1
        output = [start]
        while adj_dict:
            adj = adj_dict[start].pop()
            adj_dict[adj].remove(start)
            if len(adj_dict[start]) == 0:
                adj_dict.pop(start)
            if len(adj_dict[adj]) == 0:
                adj_dict.pop(adj)
            output.append(adj)
            start = adj
        
        return output
