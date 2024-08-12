class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            max_count = 1
            for j in range(i):
                if nums[i] > nums[j] and max_count < dp[j] + 1:
                    max_count = dp[j] + 1
            dp[i] = max_count
        return max(dp)