class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        start, end = 0, 1
        c_dict = {s[0]: 0}
        max_len = 1
        cur_len = 1
        while end < len(s):
            if s[end] in c_dict:
                index = c_dict[s[end]]
                for i in range(start, index+1):
                    c_dict.pop(s[i])
                c_dict[s[end]] = end
                start = index + 1
                cur_len = end - start + 1
            else:
                c_dict[s[end]] = end
                cur_len += 1
                max_len = max(max_len, cur_len)

            end += 1
        
        return max_len