class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)
        
        # Two heaps to track candidates from both ends
        left_heap = []
        right_heap = []
        
        # Pointers to track the boundaries of the unadded pool
        left = 0
        right = n - 1
        
        # Initialize the left heap
        while left < candidates and left <= right:
            heapq.heappush(left_heap, costs[left])
            left += 1
            
        # Initialize the right heap (ensure no overlap during initialization)
        while len(right_heap) < candidates and left <= right:
            heapq.heappush(right_heap, costs[right])
            right -= 1
            
        total_cost = 0
        
        # Process k sessions
        for _ in range(k):
            # Pick from left heap if it has the smaller or equal minimum cost
            # (Ties are broken by lower index, which favors the left side)
            if left_heap and (not right_heap or left_heap[0] <= right_heap[0]):
                total_cost += heapq.heappop(left_heap)
                # If there are elements left in the middle pool, refill the heap
                if left <= right:
                    heapq.heappush(left_heap, costs[left])
                    left += 1
            else:
                total_cost += heapq.heappop(right_heap)
                # If there are elements left in the middle pool, refill the heap
                if left <= right:
                    heapq.heappush(right_heap, costs[right])
                    right -= 1
                    
        return total_cost