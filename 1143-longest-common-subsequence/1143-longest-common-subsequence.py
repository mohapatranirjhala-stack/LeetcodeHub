class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m, n = len(text1), len(text2)
        # Create a 2D table of size (m + 1) x (n + 1) initialized to 0
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Build the table bottom-up
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    # Match found: add 1 to the diagonal value
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    # No match: take the maximum of the left or top neighbor
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                    
        return dp[m][n]