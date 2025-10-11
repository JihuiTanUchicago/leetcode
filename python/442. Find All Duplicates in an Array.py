class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        results = []
        num_set = set()
        for num in nums:
            if num in num_set:
                results.append(num)
            else:
                num_set.add(num)
        return results