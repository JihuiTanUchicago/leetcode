import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
        
        val = None
        while k != 0:
            k -= 1
            val = heapq.heappop(heap)

        return -val
# import heapq
# class Solution(object):
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         min_heap = nums[:k]
#         heapq.heapify(min_heap)
#         for i in range(k, len(nums)):
#             if nums[i] > min_heap[0]:
#                 heapq.heappushpop(min_heap, nums[i])
#         return heapq.heappop(min_heap)