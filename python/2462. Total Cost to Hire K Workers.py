import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        min_heap_front, min_heap_back = [], []
        index_front, index_back = -1, len(costs)

        for i in range(candidates):
            index_front += 1
            heapq.heappush(min_heap_front, costs[index_front])
        for i in range(candidates):
            if index_back > index_front+1:
                index_back -= 1
                heapq.heappush(min_heap_back, costs[index_back])
            else:
                break

        total_cost = 0
        worker1, worker2 = float('inf'), float('inf')
        for i in range(k):
            if worker1 == float('inf') and min_heap_front != []:
                worker1 = heapq.heappop(min_heap_front)
            if worker2 == float('inf') and min_heap_back != []:
                worker2 = heapq.heappop(min_heap_back)
            if worker1 <= worker2:
                total_cost += worker1
                if index_front < index_back-1:
                    index_front += 1
                    heapq.heappush(min_heap_front, costs[index_front])
                worker1 = float('inf')
            else:
                total_cost += worker2
                if index_back > index_front+1:
                    index_back -= 1
                    heapq.heappush(min_heap_back, costs[index_back])
                worker2 = float('inf')
                
        return total_cost