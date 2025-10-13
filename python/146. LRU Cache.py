from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache.pop(key)
            self.cache[key] = val
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.pop(key)
            self.cache[key] = value
            return
        if len(self.cache) == self.capacity:
            first_key = None
            for k in self.cache:
                first_key = k
                break
            self.cache.pop(first_key)

        self.cache[key] = value
# from collections import OrderedDict
# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.dic = OrderedDict()

#     def get(self, key: int) -> int:
#         if key not in self.dic:
#             return -1
#         self.dic.move_to_end(key)
#         return self.dic[key]

#     def put(self, key: int, value: int) -> None:
#         if key in self.dic:
#             self.dic.move_to_end(key)
#         elif len(self.dic) == self.capacity:
#             self.dic.popitem(False)
#         self.dic[key] = value



# # Your LRUCache object will be instantiated and called as such:
# # obj = LRUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)