class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (right+left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
                mid = (right+left) // 2
            else:
                right = mid - 1
                mid = (right+left) // 2
        if left >= len(nums):
            return len(nums)
        if right < 0:
            return 0
        return left
        
        
        
        