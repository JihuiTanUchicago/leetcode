class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [0 for i in range(len(nums))]
        furthest = 0
        for i in range(len(nums)):
            if furthest < i + nums[i]:
                max_range = min(i+nums[i]+1, len(nums))
                dp[furthest+1: max_range] = [dp[i]+1 for j in range(furthest+1, max_range)]
                furthest = i + nums[i]
                if furthest >= len(nums)-1:
                    break
        return dp[-1]
        