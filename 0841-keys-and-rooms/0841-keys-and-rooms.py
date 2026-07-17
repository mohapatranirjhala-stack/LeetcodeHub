class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        stack = [0]
        
        # Perform DFS traversal using a stack
        while stack:
            current_room = stack.pop()
            for key in rooms[current_room]:
                if key not in visited:
                    visited.add(key)
                    stack.append(key)
                    
        # If the number of visited rooms equals the total number of rooms
        return len(visited) == len(rooms)