class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high
        
        # Step 2: Binary search for the minimum feasible speed
        while low <= high:
            mid = low + (high - low) // 2
            
            # Calculate total hours spent eating at 'mid' speed
            hours_spent = 0
            for pile in piles:
                hours_spent += (pile + mid - 1) // mid
                
            # If Koko can finish within h hours, try a slower speed
            if hours_spent <= h:
                ans = mid
                high = mid - 1
            else:
                # Speed is too slow, increase it
                low = mid + 1
                
        return ans