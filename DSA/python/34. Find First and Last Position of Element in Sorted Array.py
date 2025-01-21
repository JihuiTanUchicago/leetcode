class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        startRange, endRange = len(nums)-1, -1
        def findTarget(left, right):
            nonlocal startRange, endRange
            if left > right:
                return
            mid = (left + right) // 2
            if nums[mid] == target:
                startRange = min(startRange, mid)
                endRange = max(endRange, mid)
                findTarget(left, mid-1)
                findTarget(mid+1, right)
            elif nums[mid] > target:
                right = mid - 1
                findTarget(left, right)
            else:
                left = mid + 1
                findTarget(left, right)
        findTarget(0, len(nums)-1)
        if endRange == -1:
            return [-1, -1]
        else:
            return [startRange, endRange]
