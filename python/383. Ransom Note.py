from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter_ransom = Counter(ransomNote)
        counter_magazine = Counter(magazine)
        for key, val in counter_ransom.items():
            if counter_magazine.get(key, 0) < val:
                return False
        return True