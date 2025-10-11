class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = [0] * len(spells)
        potions.sort()
        spells_with_index = list(zip(spells, [i for i in range(len(spells))]))
        spells_with_index.sort(reverse = True, key=lambda x: x[0])

        potion_index = 0
        for spell, index in spells_with_index:
            while potion_index < len(potions) and potions[potion_index] * spell < success:
                potion_index += 1
            pairs[index] = len(potions) - potion_index
        
        return pairs
