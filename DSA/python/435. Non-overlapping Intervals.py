#the key observation is to sort based on end bound
#and notice that for i where 0 <= i <= len(intervals)-2
#if intervals[i] and intervals[i+1] overllap,
#we would always prefer intervals[i], since 
#an optimal solution with intervals[i+1]
#could be substitued with intervals[i] with no influence
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x:x[1])
        count = 0
        last = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[last][1]:
                count += 1
            else:
                last = i
        return count
        
        