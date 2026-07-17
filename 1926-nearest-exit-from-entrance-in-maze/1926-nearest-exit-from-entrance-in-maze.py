class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        start_row, start_col = entrance
        
        # Initialize queue with: (row, col, current_steps)
        queue = deque([(start_row, start_col, 0)])
        
        # Mark the entrance as visited by turning it into a wall
        maze[start_row][start_col] = '+'
        
        # Direction vectors for stepping up, down, left, and right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c, steps = queue.popleft()
            
            # Check all 4 adjacent directions
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check if the neighbor cell is inside the bounds and empty
                if 0 <= nr < m and 0 <= nc < n and maze[nr][nc] == '.':
                    # If this empty cell is on the border, it's a valid exit!
                    if nr == 0 or nr == m - 1 or nc == 0 or nc == n - 1:
                        return steps + 1
                    
                    # Otherwise, mark it as visited and add it to the queue
                    maze[nr][nc] = '+'
                    queue.append((nr, nc, steps + 1))
                    
        # If the queue runs empty without finding a border cell, no exit exists
        return -1