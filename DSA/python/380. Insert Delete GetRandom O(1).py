from random import randint
class RandomizedSet:

    def __init__(self):
        self.a_dict = {}
        self.a_list = []
        self.index = 0

    def insert(self, val: int) -> bool:
        if self.a_dict.get(val, "") == "":
            self.a_dict[val] = self.index
            self.index += 1
            self.a_list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if self.a_dict.get(val, "") == "":
            return False
        index = self.a_dict[val]
        self.a_list[index] = self.a_list[-1]
        self.a_dict[self.a_list[index]] = index
        self.index -= 1
        self.a_list.pop()
        del self.a_dict[val]
        return True


    def getRandom(self) -> int:
        return self.a_list[randint(0, self.index-1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()