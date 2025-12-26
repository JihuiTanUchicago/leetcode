class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apple_sum = sum(apple)
        capacity.sort(reverse=True)
        count = 0
        i = 0
        while apple_sum > 0:
            apple_sum -= capacity[i]
            count += 1
            i += 1
        return count