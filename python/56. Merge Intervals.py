class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        results = []
        start = 0
        for i in range(len(intervals)):
            if intervals[start][1] >= intervals[i][0]:
                intervals[start][1] = max(intervals[start][1], intervals[i][1])
            else:
                results.append(intervals[start])
                start = i
            if i == len(intervals) - 1:
                results.append(intervals[start])
        return results