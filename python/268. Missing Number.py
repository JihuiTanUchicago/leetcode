class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        summation = sum(nums)
        supposed_summation = sum([i for i in range(1, len(nums)+1)])
        return supposed_summation - summation