class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Step 1: Build the graph
        graph = defaultdict(dict)
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1.0 / val
            
        # Step 2: Define DFS helper function to find the path product
        def dfs(start: str, end: str, visited: set) -> float:
            # If the destination is reached, the multiplier factor is 1.0
            if start == end:
                return 1.0
            
            visited.add(start)
            
            # Explore neighbors
            for neighbor, weight in graph[start].items():
                if neighbor not in visited:
                    product = dfs(neighbor, end, visited)
                    if product != -1.0:
                        return weight * product
                    
            return -1.0

        # Step 3: Process each query
        results = []
        for src, dst in queries:
            # If either variable is completely unknown, it's an immediate -1.0
            if src not in graph or dst not in graph:
                results.append(-1.0)
            else:
                results.append(dfs(src, dst, set()))
                
        return results