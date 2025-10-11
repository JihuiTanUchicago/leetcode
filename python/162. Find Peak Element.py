class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        #has to notice the property: nums[i] != nums[i + 1] for all valid i.
        start = 0
        end = len(nums) - 1
        mid = (end-start) // 2
        while start <= end:
            if start == end:
                return mid
            elif mid == start:
                if nums[mid] > nums[mid+1]:
                    return mid
                else:
                    return mid + 1 
            elif mid == end:
                if nums[mid] > nums[mid-1]:
                    return mid
                else:
                    return mid - 1
            elif nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid-1] >= nums[mid+1]:
                end = mid-1
            else:
                start = mid+1
            mid = start + (end-start) // 2