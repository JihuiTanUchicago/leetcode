class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        results = []
        start = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1] + 1:
                if start == i-1:
                    string = str(nums[start])
                else:
                    string = str(nums[start]) + "->" + str(nums[i-1])
                results.append(string)
                start = i

            if i == len(nums)-1:
                if start == i:
                    string = str(nums[start])
                else:
                    string = str(nums[start]) + "->" + str(nums[i])
                results.append(string)
        return results