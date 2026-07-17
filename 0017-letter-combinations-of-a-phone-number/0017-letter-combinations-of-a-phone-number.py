class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        # Telephone keypad digit-to-letter mapping
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        combinations = []
        
        def backtrack(index: int, path: List[str]):
            # If the combination is complete
            if len(path) == len(digits):
                combinations.append("".join(path))
                return
            
            # Get the letters that the current digit maps to
            possible_letters = phone_map[digits[index]]
            
            # Loop through the available letters
            for letter in possible_letters:
                path.append(letter)       # Choose the letter
                backtrack(index + 1, path) # Move to the next digit
                path.pop()                # Backtrack and try the next letter
                
        # Start the backtracking process from index 0
        backtrack(0, [])
        return combinations