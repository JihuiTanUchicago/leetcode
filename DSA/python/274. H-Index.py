class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sorted_citations = sorted(citations)
        h_index = 0
        for i in range(len(sorted_citations)):
            h_index = max(h_index, min(sorted_citations[i], len(sorted_citations)-i))
        return h_index