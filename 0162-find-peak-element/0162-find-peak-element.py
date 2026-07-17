class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        
        while low < high:
            mid = low + (high - low) // 2
            
            # If the current element is less than the next element, 
            # we are on an upward slope, meaning a peak is to the right.
            if nums[mid] < nums[mid + 1]:
                low = mid + 1
            # Otherwise, we are on a downward slope, meaning a peak is 
            # either at 'mid' or to the left.
            else:
                high = mid
                
        # 'low' and 'high' converge to the peak element index
        return low