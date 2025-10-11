from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        cum_sum = 0
        sum_dict = defaultdict(int)
        sum_dict[0] = 1
        for i in range(len(nums)):
            cum_sum += nums[i]
            count += sum_dict[cum_sum-k]
            sum_dict[cum_sum] += 1
        return count