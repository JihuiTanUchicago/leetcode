import math
import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        head, tail = 0, len(nums) - 1
        while head < tail:
            mid = math.floor((tail + head) / 2)
            if head == mid or tail == mid:
                if nums[head] > nums[tail]:
                    head = tail
                break
            if nums[tail] < nums[mid] < nums[head]:
                head = mid + 1
            elif nums[head] < nums[mid] < nums[tail]:
                tail = mid - 1
            elif nums[tail] < nums[head] < nums[mid]:
                head = mid
            elif nums[mid] < nums[tail] < nums[head]:
                tail = mid
            else:
                raise ValueError("I don't think it's possible bruh")
        
        nums = nums[head:] + nums[:head]
        index = bisect.bisect_left(nums, target)

        if index < len(nums):
            return (index + head) % len(nums) if nums[index] == target else -1
        return -1
