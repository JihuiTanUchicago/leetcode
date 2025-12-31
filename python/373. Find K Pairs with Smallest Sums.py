import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_heap = []
        start1 = 0
        start2 = 0
        candidates = set()
        count = 1
        heapq.heappush(min_heap, (nums1[start1]+nums2[start2], nums1[start1], nums2[start2]))
        visited = {(start1, start2)}
        while count != k:
            if start1+1 < len(nums1) and (start1+1, start2) not in visited:
                candidates.add((start1+1,start2))
            if start2+1 < len(nums2) and (start1, start2+1) not in visited:
                candidates.add((start1,start2+1))
            min_index1, min_index2 = -1, -1
            min_sum = float('inf')
            for candidate in candidates:
                a, b = candidate
                summation = nums1[a] + nums2[b]
                if summation < min_sum:
                    min_index1, min_index2 = a, b
                    min_sum = summation
            heapq.heappush(min_heap, (min_sum, nums1[min_index1], nums2[min_index2]))
            candidates.remove((min_index1, min_index2))
            visited.add((min_index1, min_index2))
            start1, start2 = min_index1, min_index2
            count += 1
        
        output = []
        while min_heap:
            summation, a, b = heapq.heappop(min_heap)
            output.append((a,b))
        return output




