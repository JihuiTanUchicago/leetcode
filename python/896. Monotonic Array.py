class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        trend = nums[1] - nums[0]
        for i in range(2, len(nums)):
            dif = nums[i] - nums[i-1]
            if dif * trend < 0:
                return False
            if trend == 0 and dif != 0:
                trend = dif
        
        return True
        