class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        num_set = set()
        for num in arr:
            if num * 2 in num_set:
                return True
            num_set.add(num)
        return False
