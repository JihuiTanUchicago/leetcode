import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap_of_great = []
        self.max_heap_of_small = []

    def addNum(self, num: int) -> None:
        if len(self.min_heap_of_great) == 0:
            heapq.heappush(self.min_heap_of_great, num)
        elif num >= self.min_heap_of_great[0]:
            heapq.heappush(self.min_heap_of_great, num)
        else:
            heapq.heappush(self.max_heap_of_small, -num)

        if len(self.min_heap_of_great) - len(self.max_heap_of_small) > 1:
            node = heapq.heappop(self.min_heap_of_great)
            heapq.heappush(self.max_heap_of_small, -node)
        elif len(self.max_heap_of_small) - len(self.min_heap_of_great) > 1:
            node = -heapq.heappop(self.max_heap_of_small)
            heapq.heappush(self.min_heap_of_great, node)
        
    def findMedian(self) -> float:
        if (len(self.min_heap_of_great) + len(self.max_heap_of_small)) % 2 == 0:
            return (self.min_heap_of_great[0] - self.max_heap_of_small[0]) / 2
        elif len(self.min_heap_of_great) > len(self.max_heap_of_small):
            return self.min_heap_of_great[0]
        else:
            return -self.max_heap_of_small[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()