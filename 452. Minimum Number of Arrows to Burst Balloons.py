class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        #balloons with overlapping points could be shot at the same time
        start = 0
        points = sorted(points, key=lambda x:x[1])
        count = 1
        for i in range(1,len(points)):
            if points[i][0] <= points[start][1]:
                continue
            else:
                count += 1
                start = i
        return count