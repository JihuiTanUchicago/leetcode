import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        count_dict = defaultdict(int)
        for num in nums:
            count_dict[num] += 1
        for num in count_dict:
            heapq.heappush(heap, (-count_dict[num], num))
        
        output = []
        while k != 0:
            k -= 1
            output.append(heapq.heappop(heap)[1])
        
        return output

# from collections import Counter
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         counter = Counter(nums)
#         most_commons = counter.most_common(k)
#         return [l[0] for l in most_commons]