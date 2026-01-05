class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low % 2 == 0:
            low += 1
        if high % 2 == 0:
            high -= 1
        return max(0, (1 + high) // 2 - (1 + low) // 2 + 1)