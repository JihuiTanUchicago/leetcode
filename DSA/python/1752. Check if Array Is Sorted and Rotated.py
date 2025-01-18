class Solution:
    def check(self, nums: List[int]) -> bool:
        chance = 1
        for i in range(0, len(nums)):
            if nums[i] < nums[i-1]:
                if chance == 1:
                    chance -= 1
                else:
                    return False
        return True

        