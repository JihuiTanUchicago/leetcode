from collections import defaultdict
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        output_dict = defaultdict(list)
        def get_hash(string):
            hash_list = []
            for i in range(1, len(string)):
                if ord(string[i-1]) > ord(string[i]):
                    hash_list.append(26+ord(string[i])-ord(string[i-1]))
                else:
                    hash_list.append(ord(string[i])-ord(string[i-1]))
            return tuple(hash_list)
        
        for string in strings:
            hash_val = get_hash(string)
            output_dict[hash_val].append(string)
        
        output = []
        for ls in output_dict.values():
            output.append(ls)
        
        return output