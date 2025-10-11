class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        min_val = float('inf')
        for i in range(len(nums)-2):
            start, end = i+1, len(nums)-1
            while start < end:
                if start != i+1 and nums[start] == nums[start-1]:
                    start += 1
                if end != len(nums)-1 and nums[end] == nums[end+1]:
                    end -= 1
                summation = nums[i]+nums[start]+nums[end]
                if abs(summation-target) < abs(min_val-target):
                    min_val = summation
                if target < summation:
                    end -= 1
                elif summation < target:
                    start += 1
                else:
                    return target
        return min_val