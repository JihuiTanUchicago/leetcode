class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0 for i in range(len(nums))]
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False

        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1] - 1)
            if dp[i] <= 0 and i != len(nums) - 1:
                return False
        return True