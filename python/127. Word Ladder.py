from collections import Counter
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if beginWord in word_set:
            word_set.remove(beginWord)
        
        num = 1
        current_queue = [beginWord]
        next_queue = []

        while current_queue != []:
            word = current_queue.pop()
            removes = set()
            for nxt_word in word_set:
                dif = 0
                for i in range(len(word)):
                    if word[i] != nxt_word[i]:
                        dif += 1
                        if dif > 1:
                            break
                if dif == 1:
                    if nxt_word == endWord:
                        return num + 1
                    next_queue.append(nxt_word)
                    removes.add(nxt_word)
            word_set -= removes
            
            if current_queue == []:
                current_queue = next_queue
                next_queue = []
                num += 1
        
        return 0
                
