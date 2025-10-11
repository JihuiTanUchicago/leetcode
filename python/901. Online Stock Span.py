class StockSpanner:
    def __init__(self):
        self.monotonic_stack = []

    def next(self, price: int) -> int:
        if self.monotonic_stack == [] or price < self.monotonic_stack[-1][0]:
            self.monotonic_stack.append([price,1])
            return 1
        else:
            count = self.monotonic_stack[-1][1] + 1
            self.monotonic_stack[-1] = [price, count]
            while len(self.monotonic_stack) > 1 and self.monotonic_stack[-1][0] >= self.monotonic_stack[-2][0]:
                count += self.monotonic_stack[-2][1]
                self.monotonic_stack[-1] = [price, self.monotonic_stack[-2][1] + self.monotonic_stack.pop()[1]]
            return count


        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)