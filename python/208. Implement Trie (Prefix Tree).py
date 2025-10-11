class Trie:

    def __init__(self):
        self.trie_dict = {}

    def insert(self, word: str) -> None:
        if word != "" or word != None:
            word += "/"
            start = self.trie_dict
            for i in range(len(word)):
                start[word[i]] = start.get(word[i],{})
                start = start[word[i]]
    def search(self, word: str) -> bool:
        if word == "" or word == None:
            return True
        word += "/"
        start = self.trie_dict
        for i in range(len(word)):
            if start.get(word[i], "N/A") == "N/A":
                return False
            start = start[word[i]]
        return True
        
    def startsWith(self, prefix: str) -> bool:
        if prefix == "" or prefix == None:
            return True
        start = self.trie_dict
        for i in range(len(prefix)):
            if start.get(prefix[i], "N/A") == "N/A":
                return False
            start = start[prefix[i]]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)