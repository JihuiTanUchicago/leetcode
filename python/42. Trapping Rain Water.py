class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = []
        right_max = []
        left_max.append(0)
        right_max.append(0)
        for i in range(1, len(height)):
            left_max.append(max(height[i-1], left_max[i-1]))
            right_max.append(max(height[-i], right_max[i-1]))
        right_max = right_max[::-1]
        summation = 0
        for i in range(len(height)):
            if left_max[i] > height[i] and right_max[i] > height[i]:
                summation += min(left_max[i],right_max[i]) - height[i]
        return summation