class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = 0
        ones = 0
        twos = 0
        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1
            else:
                twos += 1

        for i in range(len(nums)):
            if i < zeros:
                nums[i] = 0
            elif zeros <= i < zeros+ones:
                nums[i] = 1
            else:
                nums[i] = 2
        
        
            