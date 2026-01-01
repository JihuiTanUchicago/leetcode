from collections import Counter, defaultdict

class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = Counter(word)
        freq = defaultdict(int)
        for count in counter.values():
            freq[count] += 1
        
        if len(freq) > 2:
            return False
        if len(freq) == 1:
            if freq[1] > 0:
                return True
            value = list(freq.values())[0]
            if value == 1:
                return True

            return False

        freq_list = sorted(list(freq.items()))
        freq1, count1 = freq_list[0]
        freq2, count2 = freq_list[1]

        if freq1 == 1 and count1 == 1:
                return True
        if freq2 - freq1 != 1:
            return False

        if count2 > 1:
            return False
        
        return True
