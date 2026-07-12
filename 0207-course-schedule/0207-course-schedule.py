class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=[[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        for dest,src in prerequisites:
            graph[src].append(dest)
            indegree[dest]+=1
        queue=deque([i for i in range(numCourses) if indegree[i]==0])
        count=0
        while queue:
            node=queue.popleft()
            count+=1
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor]==0:
                    queue.append(neighbor)
        return count == numCourses
        