class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        appeared = set()
        for num in nums:
            if num in appeared:
                return num
            else:
                appeared.add(num)
        