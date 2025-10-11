class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        nums.sort()
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > target/4:
                break
            complement_target = target - nums[i]
            threesum_ans = self.threeSum(nums[i+1:], complement_target)
            if threesum_ans != []:
                for j in range(len(threesum_ans)):
                    output.append(threesum_ans[j] + [nums[i]])        
        return output        

    def threeSum(self, nums: List[int], target) -> List[List[int]]:
        output = []
        for i in range(len(nums)):
            if nums[i] > target / 3:
                break
            if i != 0 and nums[i] == nums[i-1]:
                continue
            complement = target - nums[i]
            two_sum_ans = self.twoSum(nums[i+1:], complement)
            if two_sum_ans != []:
                for j in range(len(two_sum_ans)):
                    output.append(two_sum_ans[j] + [nums[i]])
        return output

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output = []
        header, trailer = 0, len(numbers)-1
        while header < trailer:
            if numbers[header] + numbers[trailer] > target:
                trailer -= 1
            elif numbers[header] + numbers[trailer] < target:
                header += 1
            else:
                output.append([numbers[header], numbers[trailer]])
                header += 1
                trailer -= 1
                while header < trailer and numbers[header] == numbers[header-1]:
                    header += 1
        return output