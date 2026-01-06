class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        output = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            i_start, i_end = firstList[i]
            j_start, j_end = secondList[j]
            start = max(i_start, j_start)
            end = min(i_end, j_end)
            if start <= end:
                output.append([start, end])
            
            if i_end < j_end:
                i += 1
            else:
                j += 1
        
        return output