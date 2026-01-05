class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum = nums[0]
        max_so_far = nums[0]
        min_so_far = nums[0]
        for num in nums[1:]:    
            temp_max = max(num, max_so_far * num, min_so_far * num)
            temp_min = min(num, max_so_far * num, min_so_far * num)

            max_so_far = temp_max
            min_so_far = temp_min
            maximum = max(max_so_far, maximum)
        
        return maximum