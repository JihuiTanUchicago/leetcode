class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # Sort by end point and maintain a pointer to the latest start point
        points.sort(key=lambda x: x[1])
        count, start = 1, 0
        for i in range(1, len(points)):
            if points[start][1] < points[i][0]:
                count += 1
                start = i
        return count
