class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height) - 1
        max_area = (end - start) * min(height[start], height[end])
        while start < end:
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
            max_area = max(max_area, (end - start) * min(height[start], height[end]))

        return max_area

