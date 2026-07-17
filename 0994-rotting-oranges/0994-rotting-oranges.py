from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh_count = 0
        
        # Step 1: Collect initial rotten oranges and count fresh ones
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
                    
        # If there are no fresh oranges to begin with, 0 minutes have elapsed
        if fresh_count == 0:
            return 0
            
        minutes = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Step 2: Run BFS level by level
        while queue and fresh_count > 0:
            minutes += 1
            # Process all currently rotten oranges for this minute level
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # If neighbor is within bounds and is a fresh orange
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # Rot the orange
                        fresh_count -= 1  # Reduce fresh count
                        queue.append((nr, nc))
                        
        # Step 3: Check if any fresh orange is left unreachable
        return minutes if fresh_count == 0 else -1