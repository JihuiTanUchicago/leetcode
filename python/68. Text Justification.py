class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        new_str = []
        summation = 0
        result = []
        for word in words:
            if new_str == []:
                new_str.append(word)
                summation += len(word)
            elif summation + len(word) + 1 <= maxWidth:
                    new_str.append(word)
                    summation += len(word) + 1
            else:
                remaining_space = maxWidth - summation
                average_remain = remaining_space // max(1, (len(new_str)-1))
                leftover = remaining_space % max(1, (len(new_str)-1))
                space = (average_remain+1) * " "
                if len(new_str) == 1:
                    string = new_str[0] + " " * average_remain
                else:
                    string = (space+" ").join(new_str[:leftover+1]) + space + space.join(new_str[leftover+1:])
                result.append(string)
                new_str = [word]
                summation = len(word)
        if new_str != []:
            remaining_space = maxWidth - summation
            result.append(" ".join(new_str) + " " * remaining_space)
        return result

                
