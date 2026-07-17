class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prev2 = 0
        prev1 = 0
        
        for num in nums:
            # Decide whether to rob this house or skip it
            current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current
            
        return prev1