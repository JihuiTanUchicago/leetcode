# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        min_bad_version = n
        while left <= right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                min_bad_version = min(min_bad_version, mid)
                right = mid - 1
            else:
                left = mid + 1
        return min_bad_version