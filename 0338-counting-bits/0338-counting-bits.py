class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0] * (n + 1)
        
        for i in range(1, n + 1):
            # ans[i >> 1] is the bit count of i with its last bit removed.
            # (i & 1) is 1 if the last bit of i is set, otherwise 0.
            ans[i] = ans[i >> 1] + (i & 1)
            
        return ans