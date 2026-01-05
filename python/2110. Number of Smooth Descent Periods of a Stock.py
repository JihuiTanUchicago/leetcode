class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        intervals = []
        cur_interval = [0, 0]
        for i in range(1, len(prices)):
            if prices[i] + 1 == prices[i-1]:
                cur_interval[1] = i
            else:
                intervals.append(cur_interval)
                cur_interval = [i, i]
        intervals.append(cur_interval)
        
        count = 0
        for interval in intervals:
            length = interval[1] - interval[0] + 1
            count += (1 + length) * length // 2

        return count