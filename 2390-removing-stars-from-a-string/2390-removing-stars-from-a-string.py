class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == '*':
                # Remove the last added character (the closest to the left)
                if stack:
                    stack.pop()
            else:
                # Add the character to our stack
                stack.append(char)
                
        # Join the characters in the stack to form the final string
        return "".join(stack)