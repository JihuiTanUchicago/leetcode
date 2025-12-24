class MyCircularQueue:

    def __init__(self, k: int):
        self.queue = [-1 for i in range(k)]
        self.front_index = -1
        self.rear_index = -1
        self.capacity = 0

    def enQueue(self, value: int) -> bool:
        if self.rear_index == -1:
            self.queue[0] = value
            self.front_index = 0
            self.rear_index = 0
            self.capacity += 1
            return True
        if self.capacity >= len(self.queue):
            return False
        self.rear_index = (self.rear_index+1) % len(self.queue)
        self.queue[self.rear_index] = value
        self.capacity += 1
        return True

    def deQueue(self) -> bool:
        if self.capacity == 0:
            return False
        self.queue[self.front_index] = -1
        self.front_index = (len(self.queue) + self.front_index + 1) % len(self.queue)
        self.capacity -= 1
        return True
        

    def Front(self) -> int:
        if self.capacity == 0:
            return -1
        return self.queue[self.front_index]

    def Rear(self) -> int:
        if self.capacity == 0:
            return -1
        return self.queue[self.rear_index]

    def isEmpty(self) -> bool:
        if self.capacity == 0:
            return True
        return False

    def isFull(self) -> bool:
        if self.capacity == len(self.queue):
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()