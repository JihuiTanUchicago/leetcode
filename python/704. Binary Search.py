class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

# import bisect
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         i = bisect.bisect_left(nums, target)
#         if 0 <= i < len(nums) and nums[i] == target:
#             return i
#         return -1