class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        pos_nums = []
        neg_nums = []
        for num in nums:
            if num >= 0:
                pos_nums.append(num)
            elif num < 0:
                neg_nums.append(num)
        pos_nums.sort(reverse=True)
        neg_nums.sort()
        if len(pos_nums) == 0:
            return neg_nums[-1] * neg_nums[-2] * neg_nums[-3]
        elif len(pos_nums) == 1:
            return neg_nums[0] * neg_nums[1] * pos_nums[0]
        elif len(pos_nums) == 2:
            return neg_nums[0] * neg_nums[1] * pos_nums[0]
        else:
            if len(neg_nums) >= 2:
                return max(neg_nums[0] * neg_nums[1], pos_nums[1] * pos_nums[2]) * pos_nums[0]
            else:
                return pos_nums[0] * pos_nums[1] * pos_nums[2]
