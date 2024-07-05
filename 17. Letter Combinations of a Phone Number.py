class Solution:
    def mergeLists(self, list1, list2):
        if list1 == []:
            list1 += list2
        else:
            list1_len = len(list1)
            list1[:] = list1 * len(list2)
            for i in range(len(list2)):
                for j in range(list1_len):
                    list1[i*list1_len + j] += list2[i]
            
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        keyboard = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        results = []
        for d in digits:
            self.mergeLists(results, keyboard[d])
        return results