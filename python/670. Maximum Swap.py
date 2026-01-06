import heapq
class Solution:
    def maximumSwap(self, num: int) -> int:
        heap = []
        num_str = str(num)
        for i in range(len(num_str)):
            digit = int(num_str[i])
            heapq.heappush(heap, (-digit, i))

        for i in range(len(num_str)):
            digit = int(num_str[i])
            val, index = heapq.heappop(heap)
            val = -val
            if val == digit:
                continue
            else:
                num_str = list(num_str)
                while heap and val == -heap[0][0]:
                    val, index = heapq.heappop(heap)
                    val = -val
                num_str[i], num_str[index] = num_str[index], num_str[i]
                break
        
        num = max(num, int("".join(num_str)))
        return num
