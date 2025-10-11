from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        self.dic.move_to_end(key)
        return self.dic[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.move_to_end(key)
        elif len(self.dic) == self.capacity:
            self.dic.popitem(False)
        self.dic[key] = value



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)