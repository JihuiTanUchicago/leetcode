class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        output = []
        start = left

        while start <= right:
            start_str = str(start)
            satisfy = True
            for c in start_str:
                num = int(c)
                if num == 0:
                    satisfy = False
                    break
                if start % num != 0:
                    satisfy = False
                    break
            if satisfy:
                output.append(start)
            start += 1
        
        return output