class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        m = len(potions)
        pairs = []
        
        # Step 2: Iterate through each spell and binary search for valid potions
        for spell in spells:
            # Calculate the minimum required potion strength using ceiling integer division
            min_potion_needed = (success + spell - 1) // spell
            
            # Find the first index where the potion strength >= min_potion_needed
            idx = bisect.bisect_left(potions, min_potion_needed)
            
            # All elements from idx to the end of the array form successful pairs
            pairs.append(m - idx)
            
        return pairs