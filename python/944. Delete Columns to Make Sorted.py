class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count  = 0
        column_index = 0
        while column_index < len(strs[0]):
            row_index = 0
            while row_index < len(strs)-1:
                if ord(strs[row_index][column_index]) > ord(strs[row_index+1][column_index]):
                    count += 1
                    break
                row_index += 1
            
            column_index += 1
        
        return count