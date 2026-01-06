class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summation = float('-inf')
        max_summation = summation
        for num in nums:
            summation = max(num, summation + num)
            max_summation = max(summation, max_summation)
        return max_summation
   
# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_summation = float('-inf')
#         summation = float('-inf')
#         i = 0
#         while i < len(nums):
#             summation = max(nums[i], summation + nums[i])
#             max_summation = max(summation, max_summation)
#             i += 1

#         return max_summation
            
            
# # class Solution:
# #     def maxSubArray(self, nums: List[int]) -> int:
# #         max_sum = float('-inf')
# #         cur_sum = 0
# #         for i in range(len(nums)):
# #             if nums[i] > nums[i]+cur_sum:
# #                 cur_sum = nums[i]
# #             else:
# #                 cur_sum += nums[i]
# #             max_sum = max(max_sum, cur_sum)
# #         return max_sum
            
        
        