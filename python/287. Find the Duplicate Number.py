class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        turtle = nums[0]
        hare = nums[0]

        while True:
            turtle = nums[turtle]
            hare = nums[nums[hare]]
            if turtle == hare:
                hare = nums[0]
                break
        
        while turtle != hare:
            turtle = nums[turtle]
            hare = nums[hare]
        
        return hare
