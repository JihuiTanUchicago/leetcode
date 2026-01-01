class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] < 0:
                repeated_num = abs(nums[i])
            else:
                nums[abs(nums[i])-1] *= -1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                missing_num = i+1
                break
        
        return [repeated_num, missing_num]
                
                
