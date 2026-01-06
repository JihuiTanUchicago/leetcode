class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        abbr_expanded = ""
        num_holder = ""

        for c in abbr:
            if c.isdigit():
                if num_holder == "" and int(c) == 0:
                    return False
                num_holder += c
            else:
                if num_holder != "":
                    if int(num_holder) + len(abbr_expanded) > 20:
                        return False
                    abbr_expanded += "_" * int(num_holder)
                    num_holder = ""
                abbr_expanded += c
        if num_holder != "":
            if int(num_holder) + len(abbr_expanded) > 20:
                return False
            abbr_expanded += "_" * int(num_holder)
        if len(word) == len(abbr_expanded):
            for i in range(len(word)):
                if abbr_expanded[i] == "_":
                    continue
                if word[i] != abbr_expanded[i]:
                    return False
            return True
        else:
            return False
            