import heapq
from math import sqrt, floor
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i] = -gifts[i]
        heapq.heapify(gifts)
        for i in range(k):
            pile = -heapq.heappop(gifts)
            pile = floor(sqrt(pile))
            if pile != 0:
                heapq.heappush(gifts, -pile)
            if len(gifts) == 0:
                return 0
        return (-1) * sum(gifts)
