class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        
        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 5
            
        # Initialize variables representing dp[i-3], dp[i-2], dp[i-1]
        p3, p2, p1 = 1, 2, 5
        
        # Sequentially transition states
        for _ in range(4, n + 1):
            current = (2 * p1 + p3) % MOD
            p3 = p2
            p2 = p1
            p1 = current
            
        return p1