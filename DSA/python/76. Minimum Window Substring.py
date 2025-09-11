from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        letter_dict = defaultdict(int)
        letter_dict_copy = letter_dict.copy()
        for c in t:
            letter_dict[c] += 1
        left, right = 0, 0
        minimum_window_indexes = (float('-inf'), -1)

        def zerosOut(letter_dict):
            for key, val in letter_dict.items():
                if val > 0:
                    return False
            
            return True

        while right < len(s):
            if s[right] in letter_dict:
                letter_dict[s[right]] -= 1
            while zerosOut(letter_dict):
                min_left, min_right = minimum_window_indexes
                if min_right-min_left > right-left:
                    minimum_window_indexes = (left, right)
                if s[left] in letter_dict:
                    letter_dict[s[left]] += 1
                left += 1
            
            right += 1
        
        min_left, min_right = minimum_window_indexes
        if min_left == float('-inf'):
            return ""
        return s[min_left:min_right+1]
