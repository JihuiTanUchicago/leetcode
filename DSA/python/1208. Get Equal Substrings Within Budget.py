class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        dif = [abs(ord(s[i])-ord(t[i])) for i in range(len(s))]
        print(dif)
        prefix_sum = [0 for i in range(len(dif))]
        for i in range(len(dif)):
            if i == 0:
                prefix_sum[i] = dif[i]
            else:
                prefix_sum[i]= prefix_sum[i-1] + dif[i]
        print(prefix_sum)

        max_length = 0
        start, end = 0, 0
        while start < len(s):
            print(start, end)
            if prefix_sum[end] - prefix_sum[start] + dif[start] <= maxCost:
                end += 1
                if end == len(s):
                    max_length = max(max_length, end-start)
                    break
            else:
                max_length = max(max_length, end-start)
                start += 1
                if end < start:
                    end += 1
        return max_length