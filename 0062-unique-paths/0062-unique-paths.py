class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        row = [1] * n
        
        # Iterate through the rest of the rows
        for i in range(1, m):
            for j in range(1, n):
                # The paths to current cell = paths from left cell + paths from top cell
                # row[j] is the top cell (from the previous row iteration)
                # row[j-1] is the left cell (already updated in the current row iteration)
                row[j] = row[j] + row[j - 1]
                
        return row[-1]