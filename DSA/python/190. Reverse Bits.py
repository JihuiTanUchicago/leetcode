class Solution:
    def reverseBits(self, n: int) -> int:
        reverse_binary = bin(n)[2:]
        reverse_binary = ("0" * (32-len(reverse_binary)) + reverse_binary)[::-1]
        return int(reverse_binary, 2)
        