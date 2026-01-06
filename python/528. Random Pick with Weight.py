import random
import bisect
class Solution:

    def __init__(self, w: List[int]):
        summation = sum(w)
        self.cdf = [0 for i in range(len(w))]
        self.cdf[0] = w[0] / summation
        for i in range(1, len(w)):
            self.cdf[i] = self.cdf[i-1] + w[i] / summation

    def pickIndex(self) -> int:
        r = random.random()
        index = bisect.bisect_left(self.cdf, r)
        return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()