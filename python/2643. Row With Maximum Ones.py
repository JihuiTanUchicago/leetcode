class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_ones = -1
        max_index = -1
        for i in range(len(mat)):
            count = mat[i].count(1)
            if count > max_ones:
                max_ones = count
                max_index = i
        return [max_index, max_ones]
