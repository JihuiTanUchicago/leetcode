from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        most_commons = counter.most_common(k)
        return [l[0] for l in most_commons]