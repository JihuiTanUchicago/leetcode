class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        header, trailer = 0, len(numbers)-1
        while header < trailer:
            if numbers[header] + numbers[trailer] > target:
                trailer -= 1
            elif numbers[header] + numbers[trailer] < target:
                header += 1
            else:
                return [header+1, trailer+1]