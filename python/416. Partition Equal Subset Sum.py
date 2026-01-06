class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        summation = sum(nums)
        if summation % 2 != 0:
            return False

        subset_sum = summation // 2
        dp = [False for i in range(subset_sum+1)]
        dp[0] = True
        for num in nums:
            for j in range(subset_sum, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        return dp[subset_sum]