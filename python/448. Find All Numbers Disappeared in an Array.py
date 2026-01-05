class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = set(nums)
        output = []
        for num in range(1, n+1):
            if num not in nums:
                output.append(num)
        
        return output