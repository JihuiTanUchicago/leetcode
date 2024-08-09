from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = set(nums)
        table = defaultdict(int)
        for num in nums:
            lower = table[num-1]
            upper = table[num+1]
            value = lower + upper + 1
            table[num-lower] = value
            table[num+upper] = value
        return max(list(table.values()))