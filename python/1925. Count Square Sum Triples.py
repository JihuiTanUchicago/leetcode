class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for i in range(1, n+1):
            for j in range(i, n+1):
                summation = i * i + j * j
                square_root = int(summation ** 0.5)
                if square_root <= n and square_root * square_root == summation:
                    count += 1
                    if i != j:
                        count += 1
        
        return count