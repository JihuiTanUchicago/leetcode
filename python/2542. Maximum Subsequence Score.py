import heapq
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = sorted(list(zip(nums1, nums2)), key=lambda x:x[1])
        min_heap = []
        summation = 0
        max_score = 0

        for i in range(len(nums)-1,-1,-1):
            num1, num2 = nums[i]
            summation += num1
            heapq.heappush(min_heap, num1)
            if len(min_heap) == k:
                max_score = max(max_score, summation * num2)
                summation -= heapq.heappop(min_heap)

        return max_score