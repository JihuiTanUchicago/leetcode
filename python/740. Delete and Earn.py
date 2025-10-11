class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        arr = []
        prev = nums[0]
        count = 0
        for i in nums:
            if i == prev:
                count += 1
            else:
                arr.append((prev, count))
                prev = i
                count = 1
        arr.append((prev,count))
        dp = [0 for i in range(len(arr)+1)]
        dp[0] = 0
        dp[1] = arr[0][0] * arr[0][1]
        for i in range(2, len(arr)+1):
            temp_score = arr[i-1][0] * arr[i-1][1]
            if arr[i-2][0] == arr[i-1][0] - 1:
                dp[i] = max(dp[i-1], temp_score+dp[i-2])
            else:
                dp[i] = temp_score + dp[i-1]

        return dp[-1]
