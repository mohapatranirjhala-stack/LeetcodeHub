class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for u, v in connections:
            adj[u].append((v, 1))
            adj[v].append((u, 0))
            
        visited = [False] * n
        queue = deque([0])
        visited[0] = True
        reorder_count = 0
        
        # BFS Traversal
        while queue:
            curr = queue.popleft()
            for neighbor, sign in adj[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    reorder_count += sign  # Add 1 if we are traveling along an outgoing road
                    queue.append(neighbor)
                    
        return reorder_count