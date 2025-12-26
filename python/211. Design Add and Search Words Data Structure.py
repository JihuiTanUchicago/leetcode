class WordDictionary:

    def __init__(self):
        self.db = {}

    def addWord(self, word: str) -> None:
        cur = self.db
        for i in range(len(word)):
            if cur.get(word[i], None) is None:
                cur[word[i]] = {}
            cur = cur[word[i]]
        
        cur["END"] = {}

    def search(self, word: str) -> bool:
        queue = []
        cur = self.db
        
        def dfs(i, cur):
            if i == len(word):
                if "END" in cur:
                    return True
                else:
                    return False
            else:
                c = word[i]
                if c != ".":
                    if c in cur:
                        return dfs(i+1, cur[c])
                    else:
                        return False
                else:
                    queue = list(cur.keys())
                    for c in queue:
                        if dfs(i+1, cur[c]):
                            return True
                    return False
        
        return dfs(0, cur)
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)