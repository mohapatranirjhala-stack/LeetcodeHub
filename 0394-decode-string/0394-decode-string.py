class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        current_num = 0
        
        for char in s:
            if char.isdigit():
                # Build the number (handles multi-digit integers)
                current_num = current_num * 10 + int(char)
                
            elif char == '[':
                # Store the state before entering the brackets
                stack.append((current_string, current_num))
                # Reset tracking variables for the new inner context
                current_string = ""
                current_num = 0
                
            elif char == ']':
                # Finished an inner context, retrieve the outer state
                prev_string, num = stack.pop()
                # Decode and combine
                current_string = prev_string + (num * current_string)
                
            else:
                # Normal character, add to current working string
                current_string += char
                
        return current_string