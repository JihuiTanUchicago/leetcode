from collections import defaultdict
import bisect
class TimeMap:

    def __init__(self):
        self.value_dict = defaultdict(list)
        self.time_dict = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.value_dict[key].append(value)
        self.time_dict[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        index = bisect.bisect_right(self.time_dict[key], timestamp)
        if index == 0:
            return ""
        return self.value_dict[key][index-1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)