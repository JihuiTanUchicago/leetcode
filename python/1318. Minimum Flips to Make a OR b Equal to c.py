class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a = bin(a)[2:]
        b = bin(b)[2:]
        c = bin(c)[2:]
        max_len = len(a)
        max_len = len(b) if len(b) > max_len else max_len
        max_len = len(c) if len(c) > max_len else max_len
        a = "0"*(max_len-len(a)) + a
        b = "0"*(max_len-len(b)) + b
        c = "0"*(max_len-len(c)) + c
        count = 0
        for i in range(len(a)):
            a_i = int(a[i])
            b_i = int(b[i])
            c_i = int(c[i])
            if (a_i | b_i) != c_i: 
                #00 1, 10 0, 11 0, 01 0
                if a_i == 0:
                    if b_i == 0:
                        count += 1
                    else:
                        count += 1
                else:
                    if b_i == 0:
                        count += 1
                    else:
                        count += 2 
        return count