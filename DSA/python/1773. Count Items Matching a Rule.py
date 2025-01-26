class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        matching = ["type", "color", "name"]
        rule_index = matching.index(ruleKey)
        for item in items:
            if ruleValue == item[rule_index]:
                count += 1
        return count