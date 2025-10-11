class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefixSum = []
        prefixSum.append(nums[0])
        for i in range(1, len(nums)):
            prefixSum.append(prefixSum[-1] + nums[i])
        return prefixSum