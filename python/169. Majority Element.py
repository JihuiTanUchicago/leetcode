from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        records = defaultdict(int)
        for num in nums:
            records[num] += 1
        items = records.items()
        max_key = nums[0]
        max_val = records[max_key]
        for key, val in items:
            if max_val < val:
                max_key = key
                max_val = val
        return max_key
