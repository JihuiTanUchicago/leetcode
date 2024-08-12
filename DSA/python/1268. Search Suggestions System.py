class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        suggested = []

        for i in range(len(searchWord)):
            candidates = [p for p in products if len(p) > i and p[i] == searchWord[i]]
            suggested.append(candidates[:3])
            products = candidates
            
        return suggested

        
            