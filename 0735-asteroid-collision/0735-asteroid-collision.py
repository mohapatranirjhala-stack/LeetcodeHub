class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        for ast in asteroids:
            # We only need to check for collisions if the current asteroid moves LEFT (-)
            # and the top of the stack moves RIGHT (+)
            while stack and ast < 0 and stack[-1] > 0:
                diff = ast + stack[-1]
                
                if diff < 0:
                    # The right-moving asteroid in the stack is smaller; it explodes.
                    # Pop it and keep checking the rest of the stack.
                    stack.pop()
                elif diff > 0:
                    # The right-moving asteroid in the stack is larger; current ast explodes.
                    break
                else:
                    # Both are the same size; both explode.
                    stack.pop()
                    break
            else:
                # This 'else' belongs to the 'while' loop. 
                # It executes ONLY if the loop finishes naturally without reaching a 'break'.
                # That means the current asteroid survived all collisions or didn't collide.
                stack.append(ast)
                
        return stack