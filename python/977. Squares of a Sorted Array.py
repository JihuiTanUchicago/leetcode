class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        output = []

        while left <= right:
            left_squared = nums[left] ** 2
            right_squared = nums[right] ** 2
            if left_squared > right_squared:
                output.append(left_squared)
                left += 1
            else:
                output.append(right_squared)
                right -= 1
        
        return output[::-1]
            
        