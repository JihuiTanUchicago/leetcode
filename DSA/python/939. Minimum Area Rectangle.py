class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        point_set = set(map(tuple,points))
        minArea = float('inf')
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                if points[i][0] == points[j][0] or points[i][1] == points[j][1]:
                    continue
                if points[i][0] < points[j][0] and points[i][1] > points[j][1]:
                    top_left_point = points[i]
                    bottom_right_point = points[j]
                elif points[i][0] > points[j][0] and points[i][1] < points[j][1]:
                    top_left_point = points[j]
                    bottom_right_point = points[i]
                else:
                    continue
                
                top_right_point = (points[j][0], points[i][1])
                bottom_left_point = (points[i][0], points[j][1])
                if top_right_point not in point_set or bottom_left_point not in point_set:
                    continue
                area = (points[j][0]-points[i][0]) * (points[i][1] - points[j][1])
                minArea = min(minArea, area)
        if minArea == float('inf'):
            minArea = 0
        return minArea
        