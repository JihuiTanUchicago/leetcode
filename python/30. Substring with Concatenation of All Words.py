from typing import List
from collections import defaultdict
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_length = len(words[0])
        word_map = defaultdict(int)
        for word in words:
            word_map[word] += 1
        word_map_backup = word_map.copy()
        results = []
        for i in range(len(s)-word_length*len(words)+1):
            checked = True
            for j in range(len(words)):
                word = s[i+j*word_length: i+(j+1)*word_length]
                if word_map[word] > 0:
                    word_map[word] -= 1
                else:
                    checked = False
                    word_map = word_map_backup.copy()
                    break
            if checked:
                results.append(i)
                word_map = word_map_backup.copy()
        return results