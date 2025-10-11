class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        int_len = 33 #signed bit + 1
        ans = [0 for i in range(int_len)]
        for num in nums:
            if num >= 0:
                bin_num = bin(num)[2:]
                bin_num = "0" * (int_len - len(bin_num)) + bin_num
            else:
                bin_num = bin(num)[3:]
                bin_num = "1" + "0"*(int_len-len(bin_num)-1) + bin_num
            print(bin_num)
            for i in range(int_len):
                ans[i] = ans[i] + 1 if bin_num[i] == "1" else ans[i]
        for i in range(int_len):
            ans[i] = ans[i] % 3
        ans_bin = ""
        for bit in ans:
            ans_bin += str(bit)
        if ans_bin[0] == "1":
            return -int(ans_bin[1:], 2)
        else:
            return int(ans_bin, 2)


        