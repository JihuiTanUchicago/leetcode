class Solution:
    def mySqrt(self, x: int) -> int:
        prev_cand = 0
        cand = 1
        while cand * cand < x:
            prev_cand += 1
            cand += 1
            
