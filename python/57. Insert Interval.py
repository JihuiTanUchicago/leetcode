class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        i = 1
        while i < len(intervals):
            if intervals[i-1][1] >= intervals[i][0]:
                intervals[i-1][1] = max(intervals[i][1], intervals[i-1][1])
                intervals.pop(i)
            else:
                i += 1
        return intervals

                