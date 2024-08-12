from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)
        for string in strs:
            results[''.join(sorted(string))].append(string)
        return list(results.values())