# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

from collections import defaultdict
class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        info_dict = defaultdict(lambda: defaultdict(set))
        for i in range(len(words)-1):
            for j in range(1, len(words)):
                left_word = words[i]
                right_word = words[j]
                match_count = 0
                for k in range(6):
                    if left_word[k] == right_word[k]:
                        match_count += 1
                info_dict[left_word][match_count].add(right_word)
                info_dict[right_word][match_count].add(left_word)

        guess_set = set(words)
        match_count = float('inf')
        while match_count != 6:
            word = guess_set.pop()
            match_count = master.guess(word)
            guess_set = guess_set & info_dict[word][match_count]

        return word
