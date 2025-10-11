class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        def reverse(nums, start, end):
            while start < end:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = temp
                start += 1
                end -= 1
        reverse(nums, start = 0, end = len(nums)-1)
        reverse(nums, start = 0, end = k-1)
        reverse(nums, start = k, end = len(nums)-1)

