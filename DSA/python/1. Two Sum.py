class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum_hash = {}
        for i in range(len(nums)):
            complement_index = sum_hash.get(target-nums[i], None)
            if complement_index != None and complement_index != i:
                return [sum_hash[target-nums[i]], i]
            sum_hash[nums[i]] = i