class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left+right) // 2
            if mid % 2 == 0:
                if mid != 0 and nums[mid] == nums[mid-1]:
                    right = mid - 2
                elif mid != len(nums)-1 and nums[mid] == nums[mid+1]:
                    left = mid + 2
                else:
                    return nums[mid]
            else:
                if mid != 0 and nums[mid] == nums[mid-1]:
                    left = mid + 1
                elif mid != len(nums)-1 and nums[mid] == nums[mid+1]:
                    right = mid - 1
                else:
                    return nums[mid]


            