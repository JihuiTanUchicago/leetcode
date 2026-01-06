class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (right + left) // 2
            val = nums[mid]
            if val > target:
                right -= 1
            elif val < target:
                left += 1
            else:
                return mid
        return -1
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         left = 0
#         right = len(nums) - 1
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] == target:
#                 return mid
#             elif nums[mid] > target:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         return -1

# # import bisect
# # class Solution:
# #     def search(self, nums: List[int], target: int) -> int:
# #         i = bisect.bisect_left(nums, target)
# #         if 0 <= i < len(nums) and nums[i] == target:
# #             return i
# #         return -1