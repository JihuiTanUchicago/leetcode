class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        i = 0
        while i < len(nums)-count:
            print(nums)
            if nums[i] == val:
                count += 1
                temp = nums[i]
                nums[i] = nums[-count]
                nums[-count] = temp
            else:
                i += 1
        return len(nums) - count