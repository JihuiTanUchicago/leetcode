class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start = 0
        summation = 0
        min_length = float('inf')
        for i in range(len(nums)):
            summation += nums[i]
            while summation >= target and start <= i:
                min_length = min(min_length, i-start+1)
                if start == i:
                    break
                summation -= nums[start]
                start += 1
        if min_length == float('inf'):
            return 0
        else:
            return min_length
                