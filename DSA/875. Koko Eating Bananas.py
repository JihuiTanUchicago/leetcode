class Solution:
    def canEat(self, piles, h, k):
        for p in piles:
            h -= ceil(p/k)
        if h < 0: 
            return False
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper_bound = max(piles)
        lower_bound = 1

        while lower_bound < upper_bound:
            mid = (upper_bound + lower_bound) // 2
            if self.canEat(piles, h, mid):
                upper_bound = mid
            else:
                lower_bound = mid + 1
        return upper_bound

