import bisect
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        stop_decreasing_index = len(nums) - 1
        while stop_decreasing_index > 0:
            if nums[stop_decreasing_index-1] >= nums[stop_decreasing_index]:
                stop_decreasing_index -= 1
            else:
                break
        
        if stop_decreasing_index == 0:
            nums.reverse()
        else:
            nums[stop_decreasing_index:] = nums[stop_decreasing_index:][::-1]
            head = nums[stop_decreasing_index-1]
            swap_i = bisect.bisect_right(nums, head, lo=stop_decreasing_index, hi=len(nums)-1)
            swap_j = stop_decreasing_index - 1
            nums[swap_i], nums[swap_j] = nums[swap_j], nums[swap_i]