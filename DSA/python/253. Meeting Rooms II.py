from collections import OrderedDict
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starting_times = [interval[0] for interval in intervals]
        ending_times = [interval[1] for interval in intervals]
        starting_times.sort()
        ending_times.sort()
        start, end = 0, 0
        count = 0
        while start < len(intervals):
            if ending_times[end] > starting_times[start]:
                count += 1
            else:
                end += 1
            start += 1
            
        return count
