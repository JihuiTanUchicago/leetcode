class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if right ** (1/2) > left:
            return 0
        while left < right:
            right = right & (right - 1)
        return right
        
        