class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()
        res = []
        l, r = 0, len(products) - 1
        
        for i in range(len(searchWord)):
            char = searchWord[i]
            
            # Narrow left pointer to the first word matching prefix searchWord[0...i]
            while l <= r and (len(products[l]) <= i or products[l][i] != char):
                l += 1
                
            # Narrow right pointer to the last word matching prefix searchWord[0...i]
            while l <= r and (len(products[r]) <= i or products[r][i] != char):
                r -= 1
            
            # Collect up to 3 valid suggestions from our narrowed range [l, r]
            suggestions = []
            for j in range(l, min(l + 3, r + 1)):
                suggestions.append(products[j])
            res.append(suggestions)
            
        return res