class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0
        
        def dfs(city: int):
            # Traverse all potential neighbor cities
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)
        
        # Check every city
        for i in range(n):
            if i not in visited:
                # Found a new connected component (province)
                provinces += 1
                visited.add(i)
                dfs(i)
                
        return provinces