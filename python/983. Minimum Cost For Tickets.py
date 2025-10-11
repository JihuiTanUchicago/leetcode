class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0 for i in range(days[-1]+1)]

        i = 0
        for curDay in range(1, days[-1]+1):
            if curDay < days[i]:
                dp[curDay] = dp[curDay-1]
            else:
                i += 1
                dp[curDay] = min(
                    dp[curDay-1] + costs[0],
                    dp[max(0, curDay-7)] + costs[1],
                    dp[max(0, curDay-30)] + costs[2]
                )
        
        return dp[-1]


