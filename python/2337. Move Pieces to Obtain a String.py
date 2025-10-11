class Solution:
    def canChange(self, start: str, target: str) -> bool:
        #observation 1: orders of letters ignoring space have to match
        #observation 2: keep track of maximum space that a letter can move
        if start.replace('_', '') != target.replace('_', ''):
            return False
        target_index = 0
        space_count = 0
        for i in range(len(start)):
            if start[i] != '_':
                while target[target_index] != start[i]:
                    target_index += 1
                if start[i] == 'L' and target_index > i:
                    return False
                if start[i] == 'R' and target_index < i:
                    return False
                target_index += 1
        return True