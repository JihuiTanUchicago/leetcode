import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.min_heap = []
        self.set = set()
        self.count = 1
        heapq.heapify(self.min_heap)

    def popSmallest(self) -> int:
        if self.min_heap == []:
            self.count += 1
            return self.count - 1
        else:
            a = heapq.heappop(self.min_heap)
            self.set.remove(a)
            return a

    def addBack(self, num: int) -> None:
        if(num < self.count):
            set_len = len(self.set)
            self.set.add(num)
            if len(self.set) > set_len:
                heapq.heappush(self.min_heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)