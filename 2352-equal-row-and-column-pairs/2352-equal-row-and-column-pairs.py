class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counts = Counter(tuple(row) for row in grid)
        
        pair_count = 0
        n = len(grid)
        
        # Step 2: Iterate through each column
        for col_idx in range(n):
            # Extract the current column
            column = tuple(grid[row_idx][col_idx] for row_idx in range(n))
            
            # If this column matches any rows, add the frequency to total
            pair_count += row_counts[column]
            
        return pair_count