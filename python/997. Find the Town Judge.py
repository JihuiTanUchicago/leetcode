from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_map = defaultdict(set)
        for ls in trust:
            a, b = ls[0], ls[1]
            trust_map[a].add(b)

        candidates = set()
        for i in range(1, n+1):
            if len(trust_map[i]) == 0:
                candidates.add(i)
        
        exclude = set()
        for candidate in candidates:
            found = True
            for i in range(1, n+1):
                if i == candidate:
                    continue
                if candidate not in trust_map[i]:
                    found = False
                    break
            
            if found:
                return candidate
        
        return -1

