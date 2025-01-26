class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        output = set()
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    output.add(words[i])
                if words[j] in words[i]:
                    output.add(words[j])
        return list(output)
        