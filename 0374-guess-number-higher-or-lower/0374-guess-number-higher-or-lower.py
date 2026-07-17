# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        
        while low <= high:
            # Calculate mid to avoid overflow issues
            mid = low + (high - low) // 2
            res = guess(mid)
            
            if res == 0:
                return mid
            elif res == -1:
                # The pick is smaller, look in the lower half
                high = mid - 1
            else:
                # The pick is larger, look in the upper half
                low = mid + 1
                
        return -1